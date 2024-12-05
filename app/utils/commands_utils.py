import sys

def exit_cmd(arg: str):
    if arg.isdigit():
        sys.exit(int(arg))
    else:
        return 0

def echo_cmd(arg):
    try:
        sys.stdout.write(f"{arg}\n")
        return 1
    except Exception:
        return 0
