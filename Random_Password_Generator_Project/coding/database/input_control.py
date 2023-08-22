from data import OperationalVariables
from menu_control import *


class InputAndOutputControl:

    @staticmethod
    def input_desired_length():
        ...

    @staticmethod
    def input_desired_operation():
        
        OperationalVariables.input_desired_operation = input(
            f"{color_blue} Please enter your desired {color_red} Operation Number : "
        )
