import sys
import os
import subprocess

from app.utils.helper_funcs import find_file

"""
This class handles the execution of shell commands.
"""
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
        """
        Exit the shell with the given exit code.
        :param arg: The exit code to exit with.
        :return: None
        """
        if arg.isdigit():
            sys.exit(int(arg))
        elif arg == "":
            sys.exit(0)

    def echo_cmd(self, arg: str):
        """
        Print the given argument to the standard output.
        :param arg: The argument to print.
        :return: None
        """
        sys.stdout.write(f"{arg}\n")

    def type_cmd(self, arg: str):
        """
        Print the type of the given command.
        :param arg: The command to check the type of.
        :return: None
        """
        if arg in self.commands_map:
            sys.stdout.write(f"{arg} is a shell builtin\n")
        elif found_file := find_file(arg, self.path):
            # Print the path to the found file
            sys.stdout.write(f"{arg} is {found_file}\n")
        else:
            sys.stdout.write(f"{arg}: not found\n")

    def pwd_cmd(self, arg: str):
        """
        Print the current working directory.
        :param arg: The arguments passed to the command.
        :return: None
        """
        if arg:
            sys.stdout.write(f"pwd: too many arguments\n")
        else:
            sys.stdout.write(f"{os.getcwd()}\n")

    def cd_cmd(self, arg: str):
        """
        Change the current working directory.
        - Handles absolute and relative paths.
        - Handles the special cases of "~" and "-".
        :param arg: The directory to change to.
        :return: None
        """
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
        """
        Run the given command.
        :param full_command: The command to run.
        :return: None
        """
        if full_command[0] in self.commands_map:
            self.commands_map[full_command[0]](" ".join(full_command[1:]))
        else:
            if executable_file := find_file(full_command[0], self.path):
                # Run the executable file, external command
                subprocess.run([executable_file] + full_command[1:], stdout=sys.stdout, stderr=sys.stderr)
            else:
                sys.stdout.write(f"{full_command[0]}: not found\n")
