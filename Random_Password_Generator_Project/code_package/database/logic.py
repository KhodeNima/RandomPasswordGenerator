from .data import *


def _generate(_what_to_generate_from: list[Any]) -> str:
    """Generate random characters based on the list given

    Args:
        _what_to_generate_from (list[str]): The list of characters


    Raises:
        ValueError : If not the passed argument Is a list


    Returns:
        str : The random character's generated


    ----- This Functions Is not for global use , It is only to be used in generate_random_password function.
    """

    if not type(_what_to_generate_from) is list:
        raise ValueError(value_type_error_message.format("_what_to_generate_from"))

    password = ""
    for i in range(OperationalVariables.input_desired_length):
        password = password + str(choice(_what_to_generate_from))

    return password


def generate_random_password() -> str:
    """Generate random password's based on the OperationVariables

    Returns:
        string: The generated password
    """

    if OperationalVariables.generate_all_options_password:
        return _generate(
            _what_to_generate_from=OperationalVariables.iterable_all_elements
        )

    if OperationalVariables.generate_lowercase_password:
        return _generate(
            _what_to_generate_from=OperationalVariables.iterable_lowercase_letters
        )

    if OperationalVariables.generate_uppercase_password:
        return _generate(
            _what_to_generate_from=OperationalVariables.iterable_uppercase_letters
        )

    if OperationalVariables.generate_numeric_password:
        return _generate(_what_to_generate_from=OperationalVariables.iterable_numbers)

    else:
        return None
