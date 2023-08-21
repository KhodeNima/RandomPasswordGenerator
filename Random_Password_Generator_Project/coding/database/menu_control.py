from data import *


class Menu:

    def __init__(self, operations_numbers : list, operations_names : list , current_password : str = None):
        self.operations_numbers = operations_numbers
        self.operations_names = operations_names
        self.current_password = current_password

        if not operations_names:
            raise ValueError("The argument for the parameter ( operations_names ) Is not provided.")
        if not operations_numbers:
            raise ValueError("The argument for the parameter ( operations_names ) Is not provided. ")          
        if not type(operations_numbers) is list:
            raise ValueError("The Parameter type for the argument ( argument_numbers ) Is not valid.")
        if not type(operations_names) is list:
            raise ValueError("The parameter type for the argument ( operations_names ) Is not valid.")         
        
    def show_operations_list(self) -> str:
        """Show a list of a all avaliable operation's Refrenced by their number's
        """

        exponential_index = 0
        operations_length = len(self.operations_names)

        while exponential_index < operations_length:     
            print(f'{color_red}{self.operations_numbers[exponential_index]}{color_blue} : {color_green}{self.operations_names[exponential_index]}{color_blue}')
            exponential_index += 1

    def show_current_password(self):
        """Show the current generated password
        """

        if self.current_password == None:
            print("No generated password.")
            return None
        
        print(f"{color_blue} Your current Password Is : {color_green}{self.current_password} {color_blue}")
