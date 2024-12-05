import sys


class CommandsHandler:
    def __init__(self):
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
        else:
            sys.stdout.write(f"{arg}: not found\n")
