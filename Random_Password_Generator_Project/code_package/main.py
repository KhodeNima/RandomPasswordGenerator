"""RandomPasswordGenerator : By KhodeNima
2023/8/31
"""


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
        current_menu.show_operations_list()
        current_menu.evaluate_new_password(generate_random_password())
        current_menu.show_current_password()

        current_input.input_desired_operation(
            f"{color_blue} Please enter your desired operation{color_red} Number : {color_blue} "
        )

        if OperationalVariables.operation_is_invalid:
            clean()
            print(
                f"{color_red} This operation number is invalid! Please try again! {color_blue}"
            )
            sleep(3)
            continue

        if OperationalVariables.decided_to_quit:
            InputControl.confirm_quit_input(
                f"{color_red} Are you sure you would like to quit ? ( Yes or no only ) : "
            )

            if OperationalVariables.input_confirm_to_quit.lower() == "no":
                clean()
                print("Returning to the main menu then.")
                sleep(4)
                continue

            if (
                OperationalVariables.confirmation_is_invalid
                and not OperationalVariables.confirmed_to_quit
            ):
                clean()
                print(f"That answer Is invalid , Diverting to the menu...{color_blue}")
                sleep(4)
                continue

            if (
                OperationalVariables.confirmation_is_valid
                and OperationalVariables.confirmed_to_quit
            ):
                goodbye_screen()
                sys.exit()

        current_input.input_desired_length(
            "Please enter the lengh for your password : "
        )

        if OperationalVariables.length_is_invalid:
            clean()
            print(f"{color_red} The entered lengh is not valid , Please try again.")
            sleep(5)


if __name__ == "__main__":
    main()
