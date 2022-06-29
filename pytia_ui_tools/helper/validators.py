"""
    Helper functions for validations.
"""

import re


def validate_number(input_value: str, dot_only: bool = False) -> str:
    """
    Validates the input. Returns the validated number.

    Args:
        input (str): The input that needs validation.
        dot_only (bool, optional): Replaces comma with dot. Defaults to False.

    Returns:
        Optional[str]: The validated input.
    """
    if dot_only:
        value = input_value.replace(",", ".")
    else:
        value = input_value

    if not re.match(r"(\d|\d.\d)$", value):
        new_value = ""
        floating_point = False
        for character in value:
            if character.isdigit():
                new_value += character
            if character in [".", ","] and not floating_point:
                new_value += character
                floating_point = True
        return new_value
    return input_value
