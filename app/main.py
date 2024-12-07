import os
import sys

from app.utils.commands_utils import CommandsHandler


def main(env_path=None):
    commands_handler = CommandsHandler(path=env_path)

    commands_map = commands_handler.get_commands_map()
    while True:
        sys.stdout.write("$ ")

        command = input()
        full_command = command.split(' ', 1)
        if len(full_command) == 1:
            full_command.append("")

        command_lower = full_command[0].lower()
        if command_lower in commands_map:
            commands_map[command_lower](full_command[1])
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    path = os.environ.get("PATH")

    main(env_path=path)
