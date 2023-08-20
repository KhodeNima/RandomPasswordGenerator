from random import randint
from dataclasses import dataclass
from time import sleep
from sys import exit
import sys
import os

version = "Beta 1.4.0" # SEMANTIC NUMBERING


avaliable_operations = {
    1 : "Generate lowercased random password",
    2 : "Generate uppercased random password",
    3 : "Generate numeric random password",
    4 : "Generate random password containing number's , uppercased and lowercased letter's",
}


def clean() -> None:
    """Cleans the terminal
    """
    os.system('cls')


def exit() -> None:
    """Terminate the Proccess and exit the program
    """
    sys.exit()


def is_valid_length(length : int) -> bool:
    """Checks if a integer is considered a valid length for the operation
    """

    if not length > 20:
        return False
    
    return True


def is_valid_operation(input : int , operation_numbers : dict) -> bool:
    """Checks if a integer exist in the operation's numbering
    """

    if not input in operation_numbers.keys():
        return False
    
    return True


def list_elements_to_lower(list) -> list:
    """Return the copy of a list with the string element's converted to lowercase
    """

    new_list = []
    for element in list:

        if not type(element) is str:
            continue

        element = element.lower()
        new_list.append(element)

    return new_list


def list_to_string(list : list) -> str:
    """Converts a list to a string
    """

    result = ""
    for element in list:
        result += element
    
    return result


@dataclass
class Variables:
    """Keeps all the variables related to the operation
    """

    iterable_uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    iterable_lowercase_letters = list_elements_to_lower(iterable_uppercase_letters)
    iterable_numbers = list("123456789")

    uppercase_letters_length = len(iterable_uppercase_letters)
    lowercase_letters_length = len(iterable_lowercase_letters)
    numbers_length = len(iterable_numbers)


    input_desired_operation : str = None
    input_desired_length : str = None
    input_confirm_to_quit : str = None

    operation_is_invalid : bool = False
    length_is_invalid : bool = False

    operation_is_valid : bool = False
    length_is_valid : bool = False

    decided_to_quit : bool = False
    confirmed_to_quit : bool = False

    generate_lowercase_password : bool = False
    generate_uppercase_password : bool = False
    generate_numeric_password : bool = False
    generate_all_options_password : bool = False

    generated_random_password_list : list = None
    generated_random_password_string : str = None

