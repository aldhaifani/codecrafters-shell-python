import sys
from app.utils import commands_utils


def main():
    while True:
        sys.stdout.write("$ ")
        commands_map = {"echo": commands_utils.echo_cmd, "exit": commands_utils.exit_cmd}

        command = input()
        command_args = command.split(' ', 1)

        if command_args[0] in commands_map:
                commands_map[command_args[0]](command_args[1])
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
