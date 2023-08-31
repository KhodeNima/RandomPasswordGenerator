from .data import *


class InputControl:
    """Control the input and output's happening Inside the operation"""

    @staticmethod
    def input_desired_length(input_text: str) -> None:
        """Launch the length choosing operation"""

        if not input_text:
            raise ValueError(missing_argument_error_message.format("input_text"))
        if not type(input_text) is str:
            raise ValueError(value_type_error_message.format("input_text"))

        clean()
        print("{Password length can only be between 1 to 20.}")
        OperationalVariables.input_desired_length = input(input_text)

        if not is_valid_length(OperationalVariables.input_desired_length):
            OperationalVariables.length_is_invalid = True
            return None

        OperationalVariables.length_is_valid = True
        OperationalVariables.input_desired_length = int(
            OperationalVariables.input_desired_length
        )
        return None

    @staticmethod
    def input_desired_operation(input_text: str) -> None:
        """Launch the input choosing operation"""

        if not input_text:
            raise ValueError(missing_argument_error_message.format("input_message"))
        if not type(input_text) is str:
            raise ValueError(value_type_error_message.format("input_message"))

        OperationalVariables.input_desired_operation = input(input_text)

        if not is_valid_operation(input=OperationalVariables.input_desired_operation):
            OperationalVariables.operation_is_invalid = True
            return None

        OperationalVariables.operation_is_valid = True
        OperationalVariables.input_desired_operation = int(
            OperationalVariables.input_desired_operation
        )

        generate_variables = [
            variable
            for variable in dir(OperationalVariables)
            if not variable.startswith("__")
            and not variable.endswith("__")
            and variable.startswith("generate")
        ]

        for variable in generate_variables:
            setattr(OperationalVariables, variable, None)

        if OperationalVariables.input_desired_operation == 1:
            OperationalVariables.generate_lowercase_password = True
            return None

        if OperationalVariables.input_desired_operation == 2:
            OperationalVariables.generate_uppercase_password = True
            return None

        if OperationalVariables.input_desired_operation == 3:
            OperationalVariables.generate_numeric_password = True
            return None

        if OperationalVariables.input_desired_operation == 4:
            OperationalVariables.generate_all_options_password = True
            return None

        if OperationalVariables.input_desired_operation == 5:
            OperationalVariables.decided_to_quit = True
            return None

    @staticmethod
    def confirm_quit_input(input_text):
        clean()

        OperationalVariables.input_confirm_to_quit = input(input_text)

        if not is_yes_or_no(OperationalVariables.input_confirm_to_quit):
            OperationalVariables.confirmation_is_invalid = True
            return None

        OperationalVariables.confirmation_is_valid = True
        OperationalVariables.confirmation_is_invalid = False

        if OperationalVariables.input_confirm_to_quit == "yes".lower().strip():
            OperationalVariables.confirmed_to_quit = True
            return None

        if OperationalVariables.input_confirm_to_quit == "no":
            OperationalVariables.confirmed_to_quit = False
            return None
