from .data import *


class InputControl:
    """Control the input and output's happening Inside the operation
    """

    @staticmethod
    def input_desired_length(input_text : str) -> None:
        """Launch the length choosing operation
        """

        if not input_text:
            raise ValueError(missing_argument_error_message.format('input_text'))
        if not type(input_text) is str: 
            raise ValueError(value_type_error_message.format('input_text'))
        
        OperationalVariables.input_desired_length = (input(input_text))

        if not is_valid_length(OperationalVariables.input_desired_length):

            reset_all_variables()
            OperationalVariables.length_is_invalid = True
            return None
        
        reset_all_variables()
        OperationalVariables.length_is_valid = True
        input_desired_length = int(input_desired_length)
        return None
    
        
    @staticmethod
    def input_desired_operation(input_text : str) -> None:
        """Launch the input choosing operation
        """
        
        if not input_text:
            raise ValueError(missing_argument_error_message.format('input_message'))
        if not type(input_text) is str:
            raise ValueError(value_type_error_message.format('input_message'))


        OperationalVariables.input_desired_operation = input(
            input_text
        )
    
        
        if not is_valid_operation(input=OperationalVariables.input_desired_operation):
            reset_all_variables()
            OperationalVariables.operation_is_invalid = True
            return None
        
        reset_all_variables()
        OperationalVariables.operation_is_valid = True
        OperationalVariables.input_desired_operation = int(OperationalVariables.input_desired_operation)

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

        OperationalVariables.input_confirm_to_quit = (
            input(input_text)
        )

        if not is_yes_or_no(OperationalVariables.input_confirm_to_quit):
            reset_all_variables()
            OperationalVariables.confirmation_is_invalid = True
            return None
        
        reset_all_variables()
        OperationalVariables.confirmation_is_valid = True
        
        if OperationalVariables.input_confirm_to_quit == 'yes'.lower().strip():
            OperationalVariables.confirmed_to_quit = True
            return None
        
        if OperationalVariables.input_confirm_to_quit == 'no':
            OperationalVariables.confirmed_to_quit = False
            return None
            
