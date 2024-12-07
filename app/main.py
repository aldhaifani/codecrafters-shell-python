import os
import sys

from app.utils.commands_utils import CommandsHandler


def main(env_path=None):
    commands_handler = CommandsHandler(path=env_path)

    while True:
        sys.stdout.write("$ ")

        command = input()
        full_command = command.split(' ')
        if len(full_command) == 1:
            full_command.append("")

        commands_handler.run(full_command)


if __name__ == "__main__":
    path = os.environ.get("PATH")
    main(env_path=path)
