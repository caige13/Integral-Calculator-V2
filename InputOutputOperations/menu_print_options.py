# Contains the varies functions to print menu options and collect inputs from user
import string
import sympy as sp
import shared.constants as const
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
from shared.validator import has_multiple_symbols


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


def parse_expression(expression):
    try:
        return sp.parse_expr(expression, transformations='all')
    except sp.SympifyError:
        print("invalid expression provided")
        return False
    except ValueError:
        print("invalid expression provided")
        return False
    except SyntaxError:
        print("invalid expression provided")
        return False


def get_function(symbols):
    function = parse_expression(get_string_input("Enter function: "))
    while not has_multiple_symbols(symbols, function) or not function:
        print("Function must have symbols:", end=" ")
        print(*symbols, sep=", ")
        function = parse_expression(get_string_input("Enter function: "))
    print(function)
    return function


def get_integral_inputs(symbol: string, numerical_inputs=False):
    if numerical_inputs:
        inputs = {const.START: get_numerical_input(f"Enter starting point for {symbol}: "),
                  const.END: get_numerical_input(f"Enter ending point for {symbol}: ")}
    else:
        inputs = {const.START: get_string_input(f"Enter starting point for {symbol}: "),
                  const.END: get_string_input(f"Enter ending point for {symbol}: ")}

    return inputs


def get_integral_options():
    print("1. calculate Riemann sum (Midpoint, Left point, and Right point)")
    print("2. Just solve")
    return get_numerical_input("Which option? ")
