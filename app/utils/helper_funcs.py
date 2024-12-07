"""
This module contains helper functions that are used in the main application.
"""
import os


def find_file(file_name: str, path: str) -> str:
    """
    Find the given file in the given path.
    :param file_name: The name of the file to find.
    :param path: The path to search for the file in.
    :return: The full path to the file if found, otherwise None.
    """
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


def split_command(input_string: str) -> list:
    """
    Split the given input string into a list of command and arguments.
    - Handles spaces, single quotes, double quotes, and backslashes.
    :param input_string: The input string to split.
    :return: A list containing the command and arguments.
    """
    result = []
    buffer = []
    in_single_quotes = False  # Flag to track if we are inside single quotes
    in_double_quotes = False  # Flag to track if we are inside double quotes
    escape = False  # Flag to track if we're processing an escape sequence

    i = 0
    while i < len(input_string):
        char = input_string[i]

        if escape:
            # If escape is active, handle the escape sequence
            if in_double_quotes:
                if char in ['\\', '$', '"']:
                    buffer.append(char)
                else:
                    buffer.append('\\')
                    buffer.append(char)  # Treat backslash as normal
            elif in_single_quotes: # If in single quotes, treat backslash as normal
                buffer.append("\\")
                buffer.append(char)
            else:
                buffer.append(char)
            escape = False  # Reset escape flag
        elif char == "\\":
            escape = True  # Set escape flag when encountering a backslash
        elif char == "'" and not in_double_quotes:
            # Handle single quotes
            if in_single_quotes:
                in_single_quotes = False
                result.append("".join(buffer))  # End of single-quoted section
                buffer = []
            else:
                in_single_quotes = True
        elif char == "\"" and not in_single_quotes:
            # Handle double quotes
            if in_double_quotes:
                in_double_quotes = False
                if (i + 1 < len(input_string) and input_string[i + 1] == " ") or i + 1 == len(input_string):
                    # If a space follows a closing quote, split the string
                    result.append("".join(buffer))
                    buffer = []
                else:
                    # If no space follows a closing quote, continue appending to buffer
                    continue
            else:
                in_double_quotes = True
        elif char == " " and not in_single_quotes and not in_double_quotes:
            # If space outside quotes, split the string
            if buffer:
                result.append("".join(buffer))
                buffer = []
        else:
            # Normal characters or characters inside quotes, continue appending
            buffer.append(char)

        i += 1

    # Append any remaining content in buffer
    if buffer:
        result.append("".join(buffer))

    return result
