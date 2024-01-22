# Contains the varies functions to print menu options and collect inputs from user
import string
from shared import constants as const
from shared.custom_exceptions import MatchBreak


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


def get_numerical_input(message: string, integer=False):
    value = input(message)
    while not value.isnumeric() and not value.lower() in const.exit_values:
        print("You must enter a numerical value for this field")
        value = input(message)
    if value.lower() in const.exit_values:
        raise MatchBreak
    if integer:
        return int(value)
    return float(value)


def get_string_input(message):
    value = input(message)
    if value.lower() in const.exit_values:
        raise MatchBreak
    return value


def get_integral_inputs(symbol: string, get_function=False):
    inputs = {const.START: get_string_input(f"Enter starting point for {symbol}: "),
              const.END: get_string_input(f"Enter ending point for {symbol}: ")}
    if get_function:
        inputs[const.FUNCTION] = get_string_input("Enter function: ")
    return inputs


def get_single_integral_options():
    print("1. calculate Midpoint, Left point, and Right point")
    print("2. Just solve")
    return get_numerical_input("Which option? ")
