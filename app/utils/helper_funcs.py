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
    in_quotes = False
    quote_char = None
    escape = False  # To track if the previous character was a backslash

    for char in input_string:
        if escape:
            buffer.append(char)
            escape = False
        elif char == "\\":
            escape = True
        elif char in ("'", '"'):  # Handle both single and double quotes
            if in_quotes:
                if char == quote_char:
                    in_quotes = False
                    result.append("".join(buffer))
                    buffer = []
                else:
                    buffer.append(char)
            else:
                in_quotes = True
                quote_char = char
        elif char == " " and not in_quotes:
            if buffer:
                result.append("".join(buffer))
                buffer = []
        else:
            buffer.append(char)

    if buffer:  # Append any remaining text
        result.append("".join(buffer))

    return result
