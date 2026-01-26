import re
import html

class GraphBuilder:
    def __init__(self, events):
        """
        初始化 GraphBuilder，传入单个会话的 SyscallEvent 列表。
        调用 build_graph() 后，可通过 self.nodes 和 self.edges 获取构建的图数据。
        """
        self.events = events
        self.nodes = {}
        self.edges = []
        self._node_ids = {}
        self._node_count = 0
        self.fd_to_node = {}
        # 记录连接的 tuple 字符串（如果有）
        self.session_tuple = None
        # 初始接收连接的进程 PID（accept 调用的进程）
        self.session_pid = None

    # ----------------------- 小工具函数 -----------------------
    def _get_node_id(self, node_key, label, shape):
        """获取指定节点的唯一ID，如不存在则创建新节点。"""
        if node_key not in self._node_ids:
            self._node_count += 1
            node_id = f"n{self._node_count}"
            self._node_ids[node_key] = node_id
            # 存储节点标签和形状
            self.nodes[node_id] = (label, shape)
        return self._node_ids[node_key]

    @staticmethod
    def _extract_tuple(arg_str: str):
        """从 args 中抽取 'tuple=IP:port->IP:port' 或 '(<4t>IP:port->IP:port)' 这类网络端点"""
        if not arg_str:
            return None
        m = re.search(r"tuple=([^ ]+->[^ ]+)", arg_str)
        if m:
            return m.group(1)
        # 兜底：fd=25(<4t>172.17.0.2:55224->172.17.0.3:445)
        m = re.search(r"\(<[46u][^>]*>([^)]+->[^)]+)\)", arg_str)
        if m:
            return m.group(1)
        # 还有形如 name=172.17.0.2:55224->172.17.0.3:445
        m = re.search(r"name=([^ ]+->[^ ]+)", arg_str)
        if m:
            return m.group(1)
        return None

    @staticmethod
    def _extract_fd(arg_str: str):
        """提取 fd 数字（若存在），返回 int 或 None，同时返回 fd 解码后的目标串（括号里的部分）"""
        if not arg_str:
            return None, None
        m = re.search(r"\bfd=(\d+)(?:\(([^)]+)\))?", arg_str)
        if m:
            fd = int(m.group(1))
            decoded = m.group(2) if m.lastindex and m.lastindex >= 2 else None
            return fd, decoded
        return None, None

    @staticmethod
    def _extract_file_path(arg_str: str):
        """从 args 中尽可能抽取文件路径：优先 (<f>path)，其次 name=/path 或 path=/path"""
        if not arg_str:
            return None
        # (<f>/var/log/xxx)
        m = re.search(r"\(<f>([^)]+)\)", arg_str)
        if m:
            return m.group(1)
        # name=/path 或 name=delete.file(/tmp/delete.file) 这种，取括号里的绝对路径优先
        m = re.search(r"\bname=([^ ]+)", arg_str)
        if m:
            val = m.group(1)
            # name=delete.file(/tmp/delete.file) -> 取括号里的路径
            m2 = re.search(r"\((/[^)]+)\)", val)
            if m2:
                return m2.group(1)
            if val.startswith("/"):
                return val
        # path=
        m = re.search(r"\bpath=([^ ]+)", arg_str)
        if m:
            val = m.group(1)
            m2 = re.search(r"\((/[^)]+)\)", val)
            if m2:
                return m2.group(1)
            if val.startswith("/"):
                return val
        return None

    def _label_for_rw(self, sc, arg_str):
        """构造 read/write 类调用的 label，尽量保留 size/data 参数"""
        params = []
        size_match = re.search(r"\bsize=(\d+)\b", arg_str or "")
        data_match = re.search(r"\bdata=(.*?)(?=\s(?:fd=|size=|flags=|mode=|how=|addr=|tuple=)|$)", arg_str or "")
        if size_match:
            params.append(f"size={size_match.group(1)}")
        if data_match:
            safe_data = html.escape(data_match.group(1), quote=True)
            params.append(f"data={safe_data}")
        return sc + "(" + ", ".join(params) + ")" if params else sc + "()"

    def _label_for_open_like(self, sc, arg_str):
        params = []
        flags_match = re.search(r"\bflags=([^ ]+)", arg_str or "")
        mode_match = re.search(r"\bmode=([^ ]+)", arg_str or "")
        if flags_match:
            params.append(f"flags={flags_match.group(1)}")
        if mode_match:
            params.append(f"mode={mode_match.group(1)}")
        return sc + "(" + ",".join(params) + ")" if params else sc + "()"

    # ----------------------- 主流程 -----------------------
    def build_graph(self):
        if not self.events:
            return
        # 以第一个事件（accept/accept4）作为会话起点
        accept_event = self.events[0]
        self.session_pid = accept_event.pid
        new_fd = accept_event.ret
        tuple_str = self._extract_tuple(accept_event.args or "")
        self.session_tuple = tuple_str

        # 初始进程节点
        proc_name = accept_event.proc_name or "process"
        proc_label = f"{proc_name}({self.session_pid})"
        proc_node_id = self._get_node_id(f"proc:{self.session_pid}", proc_label, "ellipse")

        # 套接字节点
        socket_label = tuple_str.replace("->", " -> ") if tuple_str else (f"FD {new_fd}" if new_fd is not None else "socket")
        sock_node_key = f"socket:{tuple_str}" if tuple_str else f"socket:{new_fd}"
        sock_node_id = self._get_node_id(sock_node_key, socket_label, "diamond")

        # accept 边
        accept_label = accept_event.syscall
        if accept_event.syscall == "accept4":
            flag_match = re.search(r"flags=([^ ]+)", accept_event.args or "")
            accept_label += f"(flags={flag_match.group(1)})" if flag_match else "()"
        else:
            accept_label += "()"
        self.edges.append((proc_node_id, sock_node_id, accept_label, ""))

        # 记录新套接字 FD 与节点的映射
        if new_fd is not None and new_fd >= 0:
            self.fd_to_node[new_fd] = sock_node_id

        # 将整个 session 的事件拿来（由 session_splitter 保证范围），不再强依赖 tuple 过滤
        session_events = list(self.events)

        # 为 clone/fork/vfork 建立父子进程虚线边（保持原逻辑风格）
        seen_clone_edges = set()
        for i, ev in enumerate(session_events):
            if ev.syscall in ("clone", "fork", "vfork") and ev.ret is not None:
                # 父进程分支：ret>0（返回子pid）
                if ev.ret and ev.ret > 0:
                    parent_node_id = self._get_node_id(f"proc:{ev.pid}", f"{ev.proc_name or 'process'}({ev.pid})", "ellipse")
                    child_pid = ev.ret
                    # 尝试在后续找到子进程的那条 ret=0 的记录拿到真正的 pid（有时 ret 就是子pid）
                    for j in range(i+1, min(i+50, len(session_events))):
                        ev2 = session_events[j]
                        if ev2.syscall == ev.syscall and ev2.ret == 0:
                            # 通常 ret=0 的这一条发生在子进程，ev2.pid 就是子 pid
                            child_pid = ev2.pid
                            break
                    child_node_id = self._get_node_id(f"proc:{child_pid}", f"{ev.proc_name or 'process'}({child_pid})", "ellipse")
                    edge_key = (parent_node_id, child_node_id, ev.syscall)
                    if edge_key not in seen_clone_edges:
                        self.edges.append((parent_node_id, child_node_id, f"{ev.syscall}()", "dashed"))
                        seen_clone_edges.add(edge_key)

        # 遍历事件，生成进程 -> 资源的边
        for ev in session_events:
            sc = ev.syscall
            # 跳过 accept（已处理）
            if sc in ("accept", "accept4"):
                continue

            arg_str = ev.args or ""
            resource_node_id = None
            node_key = None
            label = None

            # 1) 优先识别网络目标（tuple 或 fd 解码的 tuple）
            sock_tuple = self._extract_tuple(arg_str)
            if sock_tuple:
                node_key = f"socket:{sock_tuple}"
                resource_node_id = self._get_node_id(node_key, sock_tuple.replace("->", " -> "), "diamond")

            # 2) 识别文件路径
            if resource_node_id is None:
                fpath = self._extract_file_path(arg_str)
                if fpath:
                    node_key = f"file:{fpath}"
                    resource_node_id = self._get_node_id(node_key, fpath, "rectangle")

            # 3) 管道
            if resource_node_id is None and "pipe:[" in arg_str:
                pipe_match = re.search(r"pipe:\[(\d+)\]", arg_str)
                if pipe_match:
                    pipe_id = pipe_match.group(1)
                    node_key = f"pipe:{pipe_id}"
                    resource_node_id = self._get_node_id(node_key, f"pipe[{pipe_id}]", "ellipse")

            # 4) 如果还没有资源节点，则通过 fd 映射来兜底（适用于 read/write/close 等）
            fd_val, fd_decoded = self._extract_fd(arg_str)
            if resource_node_id is None and fd_val is not None and fd_val in self.fd_to_node:
                resource_node_id = self.fd_to_node[fd_val]

            # 5) 依然没有资源节点就跳过（保持之前“尽量不乱连”的策略）
            if resource_node_id is None:
                continue

            # 确保源进程节点存在
            src_key = f"proc:{ev.pid}"
            if src_key not in self._node_ids:
                src_label = f"{ev.proc_name or 'process'}({ev.pid})"
                self._get_node_id(src_key, src_label, "ellipse")
            src_node_id = self._node_ids[src_key]

            # 构造边标签（尽量保留原逻辑）
            if sc in ("read", "write", "writev", "sendto", "recvfrom", "pread"):
                label = self._label_for_rw(sc, arg_str)
            elif sc in ("open", "openat", "socket", "connect"):
                if sc == "connect":
                    addr_match = re.search(r"\baddr=([^ ]+)", arg_str)
                    label = f"connect({addr_match.group(1)})" if addr_match else "connect()"
                else:
                    label = self._label_for_open_like(sc, arg_str)
            elif sc == "shutdown":
                how_match = re.search(r"\bhow=([^ ]+)", arg_str)
                label = f"shutdown({how_match.group(1)})" if how_match else "shutdown()"
            else:
                # 其他调用保留空括号，保持简洁
                label = sc + "()"

            self.edges.append((src_node_id, resource_node_id, label, ""))

            # --------- 维护 fd 到资源的映射 ----------
            # open/openat/socket 类调用返回的新 fd
            if sc in ("open", "openat", "socket") and ev.ret is not None and ev.ret >= 0:
                self.fd_to_node[ev.ret] = resource_node_id
            # accept 已在前面处理
            # pipe() 返回两个 fd，需要特殊处理：从 args 中抓两个 fd 的显示（如果日志里有）
            if sc == "pipe":
                # 有些日志会显示 fd1=22 fd2=26，尽量抓一下
                m1 = re.search(r"\bfd1=(\d+)", arg_str)
                m2 = re.search(r"\bfd2=(\d+)", arg_str)
                if m1:
                    try:
                        self.fd_to_node[int(m1.group(1))] = resource_node_id
                    except: pass
                if m2:
                    try:
                        self.fd_to_node[int(m2.group(1))] = resource_node_id
                    except: pass
            # dup2(oldfd->newfd)
            if sc == "dup2":
                m_old = re.search(r"\boldfd=(\d+)", arg_str)
                m_new = re.search(r"\bnewfd=(\d+)", arg_str)
                if m_old and m_new:
                    try:
                        oldfd = int(m_old.group(1))
                        newfd = int(m_new.group(1))
                        if oldfd in self.fd_to_node:
                            self.fd_to_node[newfd] = self.fd_to_node[oldfd]
                    except: pass
            # close 之后可以选择移除映射（但为了绘图完整性，我们保留映射，不强制删除）
