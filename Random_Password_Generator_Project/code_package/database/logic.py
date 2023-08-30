from .data import *

def _generate(_what_to_generate_from : list[Any]) -> str:
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
        raise ValueError(value_type_error_message.format('_what_to_generate_from'))

    _counter = 0
    _characters_list = []
    _characters_string = str()
    
    while _counter < int(OperationalVariables.input_desired_length):
        _first_random_number = randint(_counter,len(_what_to_generate_from) - 1)
        _second_random_number = randint(_counter, len(_what_to_generate_from) - 1)

        if _first_random_number == _second_random_number:
            _characters_list.append(_what_to_generate_from[_first_random_number])
            _counter += 1
        
    for _character in _characters_list:
        _characters_string = _characters_string + str(_character)
        
    return _characters_string
        

def generate_random_password() -> str:
    """Generate random password's based on the OperationVariables

    Returns:
        string: The generated password
    """

    if OperationalVariables.generate_all_options_password:
        return _generate(_what_to_generate_from=OperationalVariables.iterable_all_elements)

    if OperationalVariables.generate_lowercase_password:
        return _generate(_what_to_generate_from=OperationalVariables.iterable_lowercase_letters)
    
    if OperationalVariables.generate_uppercase_password:
        return _generate(_what_to_generate_from=OperationalVariables.iterable_uppercase_letters)

    if OperationalVariables.generate_numeric_password:
        return _generate(_what_to_generate_from=OperationalVariables.iterable_numbers)