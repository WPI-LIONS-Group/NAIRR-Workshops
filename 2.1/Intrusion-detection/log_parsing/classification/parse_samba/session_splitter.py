from typing import List
from log_parser import SyscallEvent
import re

def extract_tuple(args: str) -> str:
    """从 args 中提取 tuple=IP:port->IP:port 结构（用于定位连接）"""
    if not args:
        return ""
    match = re.search(r"tuple=([^ ]+->[^ ]+(?: [^ ]+)?)", args)
    return match.group(1) if match else ""

def split_sessions(events: List[SyscallEvent]) -> List[List[SyscallEvent]]:
    """
    基于时序将所有事件按 accept/accept4 分割为多个 session，
    每个 session 包含从 accept 到下一个 accept 之间的所有 syscall。
    不再依赖 fd/pid/tuple 过滤，也不再将 close(fd) 作为 session 终止条件。
    """
    sessions = []
    i = 0
    n = len(events)

    while i < n:
        ev = events[i]
        # 查找 accept/accept4 系统调用作为起点
        if ev.syscall in ("accept", "accept4") and ev.ret is not None and ev.ret >= 0:
            session = [ev]  # 包括 accept 本身
            i += 1
            while i < n:
                e = events[i]
                # 如果遇到下一个 accept，当前 session 结束
                if e.syscall in ("accept", "accept4") and e.ret is not None and e.ret >= 0:
                    break
                session.append(e)
                i += 1
            sessions.append(session)
        else:
            i += 1

    return sessions
