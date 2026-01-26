import re
from typing import List, Optional, Tuple, Dict

class SyscallEvent:
    def __init__(self, pid: int, proc_name: str, syscall: str, args: Optional[str], ret: Optional[int], fd: Optional[str]):
        self.pid = pid
        self.proc_name = proc_name
        self.syscall = syscall
        self.args = args
        self.ret = ret
        self.fd = fd

    def __repr__(self):
        return f"<SyscallEvent {self.syscall}({self.args}) -> {self.ret}>"

class LogParser:
    IGNORED_SYSCALLS = {
        "fcntl", "getsockopt", "setsockopt", "ioctl", "lseek", "lstat",
        "getuid", "geteuid", "getgid", "getegid", "getpid", "gettid",
        "brk", "mmap", "munmap", "mprotect", "mremap", "sched_yield",
        "rt_sigaction", "rt_sigprocmask", "sigreturn", "sigaltstack",
        "getrusage", "getrlimit", "getpriority", "setpriority",
        "getrandom", "memfd_create", "statfs", "fstatfs",
        "getsockname", "getpeername", "nanosleep", "clock_gettime"
    }

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.raw_lines = []
        self.merged_events = []
        self.syscall_events: List[SyscallEvent] = []

    def read_log(self) -> bool:
        try:
            with open(self.filepath, 'r') as f:
                self.raw_lines = f.readlines()
            return True
        except Exception as e:
            print(f"[Error] Failed to read file: {e}")
            return False

    def merge_lines(self):
        current_event = ""
        for line in self.raw_lines:
            line = line.rstrip('\n')
            if not line or re.match(r"^[A-Za-z]{3} ", line):
                continue
            if re.match(r"^\d{2}:\d{2}:\d{2}\.", line):
                if current_event:
                    self.merged_events.append(current_event)
                current_event = line
            else:
                current_event += " " + line.strip()
        if current_event:
            self.merged_events.append(current_event)

    def parse_events(self):
        open_events: Dict[Tuple[int, str], Dict] = {}

        for line in self.merged_events:
            pid_match = re.search(r"PID:(\d+)", line)
            if not pid_match:
                continue
            pid = int(pid_match.group(1))
            sys_match = re.search(r"Syscall:([a-zA-Z0-9_]+)", line)
            if not sys_match:
                continue
            syscall = sys_match.group(1)
            if syscall in self.IGNORED_SYSCALLS:
                continue

            name_match = re.search(r"Name:([^ ]+)", line)
            proc_name = name_match.group(1) if name_match else ""
            fd_match = re.search(r"FD:([^ ]+)", line)
            fd_str = fd_match.group(1) if fd_match else None
            ret_match = re.search(r"Return:([^ ]+)", line)
            ret_str = ret_match.group(1) if ret_match else None

            args = self.extract_args(line)
            is_enter_event = ret_str is None or ret_str == "<NA>"

            if is_enter_event:
                open_events[(pid, syscall)] = {
                    'pid': pid,
                    'proc_name': proc_name,
                    'syscall': syscall,
                    'args': args,
                    'fd': fd_str
                }
            else:
                ret_val = self.parse_return_value(ret_str)
                if (pid, syscall) in open_events:
                    entry = open_events.pop((pid, syscall))
                    entry_args = entry.get('args')
                    final_args = None

                    if entry_args and args:
                        if syscall in ("accept", "accept4", "close"):
                            final_args = entry_args + " " + args
                        else:
                            final_args = args
                    else:
                        final_args = args or entry_args

                    self.syscall_events.append(SyscallEvent(pid, proc_name, syscall, final_args, ret_val, fd_str))
                else:
                    self.syscall_events.append(SyscallEvent(pid, proc_name, syscall, args, ret_val, fd_str))

    @staticmethod
    def extract_args(line: str) -> Optional[str]:
        args_start = line.find("Args:")
        if args_start == -1:
            return None
        args_str = line[args_start + 5:]
        ret_index = args_str.find("Return:")
        if ret_index != -1:
            args_str = args_str[:ret_index].strip()
        return args_str.strip() if args_str else None

    @staticmethod
    def parse_return_value(ret_str: str) -> Optional[int]:
        if ret_str in ("<NA>", "<NONE>"):
            return None
        try:
            if ret_str.startswith("0x"):
                return None  # 指针地址类
            return int(ret_str.split("(")[0])
        except:
            try:
                return int(ret_str.split("(")[0])
            except:
                return None

    def parse(self) -> List[SyscallEvent]:
        if not self.read_log():
            return []
        self.merge_lines()
        self.parse_events()
        return self.syscall_events



# # 示例用法（建议放主脚本里）
# if __name__ == "__main__":
#     parser = LogParser("/Users/mcfly/Desktop/server-behavior-group/falco_logs/samba_base_delete.txt")
#     events = parser.parse()
#     for ev in events:
#         print(ev)