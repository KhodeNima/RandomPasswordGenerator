from secrets import choice
from dataclasses import dataclass
from time import sleep
from sys import exit
from typing import Any
import platform, inspect, os, sys

current_version = "Beta 3.5.2"

color_blue = f"\33[34m"
color_red = f"\33[31m"
color_green = f"\33[32m"

value_type_error_message = (
    "The argument type passed to the parameter ( {} ) Is not valid."
)
missing_argument_error_message = "No argument provided for the parameter ( {} )"


avaliable_operations = {
    1: "Generate lowercased random password",
    2: "Generate uppercased random password",
    3: "Generate numeric random password",
    4: "Generate random password containing number's , uppercased and lowercased letter's",
    5: "Quit the App",
}


operations_numbers_list = [number for number in avaliable_operations.keys()]
operation_titles_list = [title for title in avaliable_operations.values()]


def clean() -> None:
    """Clear the terminal"""

    current_os = platform.system()

    if current_os == "Linux":
        os.system("clear")

    elif current_os == "Windows":
        os.system("cls")


def exit() -> None:
    """Terminate the Proccess and exit the program"""
    sys.exit()


def is_valid_length(length: int) -> bool:
    """Checks if a integer is considered a valid length for the operation"""

    try:
        length = int(length)
    except:
        return False

    if not length <= 20:
        return False

    return True


def is_valid_operation(input: int) -> bool:
    """Checks If a integer Is a valid operation number"""

    try:
        input = int(input)
    except:
        return False

    if not input in avaliable_operations.keys():
        return False

    return True


def list_elements_to_lowercase(list) -> list:
    """Return the copy of a list with the string element's converted to lowercase"""

    new_list = []
    for element in list:
        if not type(element) is str:
            continue

        element = element.lower()
        new_list.append(element)

    return new_list


def list_to_string(list: list) -> str:
    """Converts a list elements to a string"""

    result = ""
    for element in list:
        result += element

    return result


def dictionary_to_list(dictionary: dict, want_to_return: str = "items") -> list:
    """Create a list based by the element's of a dictionary

    Args:
        dictionary : The assigend dictionary

        what_to_return : 'items' , 'keys' , 'values'. Default to 'items'.

    """

    new_list = []

    if not type(dictionary) is dict:
        raise ValueError(
            "The provided argumenet type for the parameter ( dictionary ) Is not Valid"
        )
    if not type(want_to_return) is str:
        raise ValueError(
            "The provided argumenet type for the parameter ( what_to_return ) Is not Valid"
        )
    if (
        not want_to_return == "items"
        and not want_to_return == "keys"
        and not want_to_return == "values"
    ):
        raise ValueError()

    if want_to_return.lower() == "items":
        new_list = [item for item_pair in dictionary.items() for item in item_pair]
        return new_list
    if want_to_return.lower() == "keys":
        new_list = [key for key in dictionary.keys()]
        return new_list
    if want_to_return.lower() == "values":
        new_list = [value for value in dictionary.values()]
        return new_list


def is_yes_or_no(string: str) -> bool:
    if not string.lower().strip() == "yes" or string.lower().strip() == "no":
        return False

    return True


@dataclass
class OperationalVariables:
    """Keeps all the variables related to the operation"""

    iterable_uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    iterable_lowercase_letters = list_elements_to_lowercase(iterable_uppercase_letters)
    iterable_numbers = list("123456789")
    iterable_all_elements = (
        iterable_uppercase_letters + iterable_lowercase_letters + iterable_numbers
    )

    uppercase_letters_length = len(iterable_uppercase_letters)
    lowercase_letters_length = len(iterable_lowercase_letters)
    numbers_length = len(iterable_numbers)

    input_desired_operation: str = None
    input_desired_length: str = None
    input_confirm_to_quit: str = None

    operation_is_invalid: bool = False
    length_is_invalid: bool = False
    confirmation_is_invalid: bool = False

    operation_is_valid: bool = False
    length_is_valid: bool = False
    confirmation_is_valid: bool = False

    decided_to_quit: bool = False
    confirmed_to_quit: bool = False

    generate_lowercase_password: bool = False
    generate_uppercase_password: bool = False
    generate_numeric_password: bool = False
    generate_all_options_password: bool = False

    generated_random_password_list: list = None
    generated_random_password_string: str = None
