import sys
from app.utils.commands_utils import CommandsHandler


def main():
    commands_handler = CommandsHandler()

    commands_map = commands_handler.get_commands_map()
    while True:
        sys.stdout.write("$ ")

        command = input()
        command_args = command.split(' ', 1)
        if len(command_args) == 1:
            command_args.append("")

        if command_args[0] in commands_map:
                commands_map[command_args[0]](command_args[1])
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
