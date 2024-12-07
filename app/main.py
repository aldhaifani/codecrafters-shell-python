import os
import sys

from app.utils.commands_utils import CommandsHandler
from app.utils.helper_funcs import split_command


"""
This is the main entry point for the shell application.
"""
def main(env_path=None):
    commands_handler = CommandsHandler(path=env_path)

    # Main shell loop
    while True:
        sys.stdout.write("$ ")

        command = input()
        # Split the command into a list of command and arguments
        # using the helper function
        full_command = split_command(command)

        if len(full_command) == 1:
            full_command.append("")

        commands_handler.run(full_command)


if __name__ == "__main__":
    path = os.environ.get("PATH")
    main(env_path=path)
