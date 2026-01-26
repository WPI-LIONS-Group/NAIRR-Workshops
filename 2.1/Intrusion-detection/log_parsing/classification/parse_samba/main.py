# main.py

from log_parser import LogParser
from session_splitter import split_sessions
from build_graph import GraphBuilder
from output import GraphWriter

if __name__ == "__main__":
    log_path = "/Users/mcfly/Desktop/server-behavior-group/falco_logs/samba/samba_base_delaywrite.txt"
    output_dir = "dot_output/base_delaywrite"  # 生成 dot 文件的目录

    # Step 1: 解析原始日志为 SyscallEvent 列表
    parser = LogParser(log_path)
    all_events = parser.parse()

    if not all_events:
        print("❌ 日志解析失败或无有效事件")
        exit(1)

    # Step 2: 拆分所有事件为若干个会话（每个以 accept 开始）
    sessions = split_sessions(all_events)
    print(f"✅ 共解析出 {len(sessions)} 个会话")

    # Step 3: 为每个会话构建图并写入 DOT 文件
    writer = GraphWriter(output_dir=output_dir)
    for i, session in enumerate(sessions):
        print(f"\n--- Session {i} ---")
        for ev in session:
            print(ev)

        # 构建行为图
        builder = GraphBuilder(session)
        builder.build_graph()

        # 写入 DOT 文件（文件名由 socket tuple 或 pid_fd 决定）
        dot_file = writer.write_dot(builder)
        print(f"🟢 Session {i} 写入图文件: {dot_file}")
