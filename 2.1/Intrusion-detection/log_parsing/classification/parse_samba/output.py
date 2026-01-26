# output.py
import os

class GraphWriter:
    def __init__(self, output_dir: str = "."):
        """
        初始化 GraphWriter，可指定输出目录（默认为当前目录）。
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def write_dot(self, graph_builder, filename: str = None):
        """
        将 GraphBuilder 构建好的图写入 DOT 文件。
        如果未提供 filename，则使用连接 tuple 或默认方案命名文件。
        返回生成的文件路径。
        """
        # 确定文件基本名
        if filename:
            base_name = filename
        else:
            if graph_builder.session_tuple:
                base_name = graph_builder.session_tuple
            else:
                pid = graph_builder.session_pid or "unknown_pid"
                new_fd = graph_builder.events[0].ret if graph_builder.events else None
                fd_str = str(new_fd) if new_fd is not None else "unknown_fd"
                base_name = f"session_{pid}_{fd_str}"
        # 替换空格等特殊字符
        base_name = base_name.replace(" ", "_")
        if not base_name.endswith(".dot"):
            base_name += ".dot"

        file_path = os.path.join(self.output_dir, base_name)
        with open(file_path, 'w') as f:
            f.write("digraph session {\n")
            f.write("    rankdir=LR;\n")
            # 输出节点定义
            for node_id, (label, shape) in graph_builder.nodes.items():
                safe_label = label.replace('"', '\\"')
                f.write(f'    {node_id} [label="{safe_label}", shape={shape}];\n')
            # 输出边定义
            for src, dst, label, style in graph_builder.edges:
                safe_label = label.replace('"', '\\"')
                # 转义换行符
                safe_label = safe_label.replace('\n', '\\n')
                style_str = f', style={style}' if style else ''
                f.write(f'    {src} -> {dst} [label="{safe_label}"{style_str}];\n')
            f.write("}\n")
        return file_path
