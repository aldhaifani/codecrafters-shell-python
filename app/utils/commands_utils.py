import sys
import os
import subprocess


class CommandsHandler:
    def __init__(self, path=None):
        self.path = path
        self.commands_map = {
            "exit": self.exit_cmd,
            "echo": self.echo_cmd,
            "type": self.type_cmd,
            "pwd": self.pwd_cmd,
            "cd": self.cd_cmd
        }
        self.prev_dir = None

    def exit_cmd(self, arg: str):
        if arg.isdigit():
            sys.exit(int(arg))
        elif arg == "":
            sys.exit(0)

    def echo_cmd(self, arg: str):
        sys.stdout.write(f"{arg}\n")

    def type_cmd(self, arg: str):
        if arg in self.commands_map:
            sys.stdout.write(f"{arg} is a shell builtin\n")
        elif found_file := find_file(arg, self.path):
            sys.stdout.write(f"{arg} is {found_file}\n")
        else:
            sys.stdout.write(f"{arg}: not found\n")

    def pwd_cmd(self, arg: str):
        if arg:
            sys.stdout.write(f"pwd: too many arguments\n")
        else:
            sys.stdout.write(f"{os.getcwd()}\n")

    def cd_cmd(self, arg: str):
        if arg:
            if arg == "~":
                arg = os.path.expanduser("~")
            if arg == "-":
                if self.prev_dir:
                    arg = self.prev_dir
                else:
                    return
            try:
                self.prev_dir = os.getcwd()
                os.chdir(arg)
            except FileNotFoundError:
                sys.stdout.write(f"cd: {arg}: No such file or directory\n")
        else:
            sys.stdout.write(f"cd: too few arguments\n")

    def run(self, full_command: list):
        if full_command[0] in self.commands_map:
            self.commands_map[full_command[0]](" ".join(full_command[1:]))
        else:
            if executable_file := find_file(full_command[0], self.path):
                self.run_external([executable_file] + full_command[1:])
            else:
                sys.stdout.write(f"{full_command[0]}: not found\n")

    def run_external(self, full_command: list):
        subprocess.run(full_command, stdout=sys.stdout, stderr=sys.stderr)


def find_file(file_name: str, path: str) -> str:
    if not path:
        return None

    if ":" in path:
        path = path.split(':')
    else:
        path = [].append(path)

    for p in path:
        if os.path.exists(f"{p}/{file_name}"):
            return f"{p}/{file_name}"

    return None
