from .data import *


class Menu:
    def __init__(self, operations_numbers: list, operations_names: list):
        self.operations_numbers = operations_numbers
        self.operations_names = operations_names

        if not operations_names:
            raise ValueError(missing_argument_error_message.format("operations_names"))
        if not operations_numbers:
            raise ValueError(
                missing_argument_error_message.format("operations_numbers")
            )
        if not type(operations_numbers) is list:
            raise ValueError(value_type_error_message.format("operations_numbers"))
        if not type(operations_names) is list:
            raise ValueError(value_type_error_message.format("operations_names"))

    def show_operations_list(self) -> str:
        """Show a list of a all avaliable operation's Refrenced by their number's"""

        clean()
        exponential_index = 0
        operations_length = len(self.operations_names)

        print(
            f"{color_blue}-------------------- {color_green}Operations list{color_blue} --------------------"
        )

        while exponential_index < operations_length:
            print(
                f"\n {color_red}{self.operations_numbers[exponential_index]}{color_blue} : {color_green}{self.operations_names[exponential_index]}{color_blue}"
            )
            exponential_index += 1

    def evaluate_new_password(self, current_password: str):
        """Set the new entry as the current menu password"""

        self.current_password = current_password

    def show_current_password(self):
        """Show the current generated password"""

        print(f"\n---------------------------------------------------------")

        print(
            f"{color_blue} Your current Password Is : {color_green}{self.current_password}{color_blue}"
        )

        print(f"---------------------------------------------------------")
