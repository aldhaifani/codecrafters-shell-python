import sys


def main():
    while True:
        sys.stdout.write("$ ")
        commands_list = ['exit']

        command = input()
        command_args = command.split()

        if command_args[0] in commands_list and command_args[0] == 'exit' and command_args[1] == '0':
            sys.exit(0)

        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
