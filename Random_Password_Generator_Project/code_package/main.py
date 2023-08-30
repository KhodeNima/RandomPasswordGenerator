from database.data import *
from database.input_control import *
from database.logic import *
from database.menu_control import *
from database.simulations import *



def main():
    """The main program running operation"""

    loading_screen()
    welcome_screen()

    current_menu = Menu(operations_numbers_list, operation_titles_list)
    current_input = InputControl()

    while True:

        reset_all_variables()
        current_menu.show_operations_list()
        current_menu.evaluate_new_password(OperationalVariables.generated_random_password_string)
        current_menu.show_current_password()

        current_input.input_desired_operation(
            f'{color_blue} Please enter your desired operation{color_red} Number : {color_blue} '
            )

        if OperationalVariables.operation_is_invalid:
            clean()
            print(f'{color_red} This operation number is invalid! Please try again! {color_blue}')
            sleep(3)
            continue
        
        clean()
        current_input.input_desired_length(
            input_text=f"{color_blue} Please enter the length for your password {color_red}( 1 TO 20 ){color_blue} : "
            )
            
        
        



if __name__ == '__main__':
    main()