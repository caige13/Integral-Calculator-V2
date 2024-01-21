# Contains the varies functions to print menu options and collect inputs from user
import string
from custom_exceptions import _MatchBreak

exit_values = ['e', 'exit', 'break', 'back', 'previous']


# def numerical_checker(value: string):
#     if not value.isnumeric():
#         raise _MatchBreak
#     return int(value)
#
#
# def value_checker(value: string):
#     if value.lower() in exit_values:
#         raise _MatchBreak
#     return value


def get_numerical_input(message: string):
    value = input(message)
    if not value.isnumeric():
        raise _MatchBreak
    return int(value)

def get_string_input(message):
    value = input(message)
    if value.lower() in exit_values:
        raise _MatchBreak
    return value


def print_menu():
    print("\nIf you're new to Python Look at Library I explain some of the operators")
    print("\n1. Single Integral Calculator")
    print("2. Double Integral Calculator")
    print("3. Triple Integral Calculator")
    print("4. Anti Derivative of a Function")
    print("5. Derivative of a Function")
    print("6. Library of Python Symbols(Have to use these)")
    print("7. Exit")
    return input("Which option? ")
