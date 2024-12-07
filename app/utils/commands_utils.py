import sys
import os


class CommandsHandler:
    def __init__(self, path=None):
        self.path = path
        self.commands_map = {
            "exit": self.exit_cmd,
            "echo": self.echo_cmd,
            "type": self.type_cmd
        }

    def get_commands_map(self):
        return self.commands_map

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
