# Caige Middaugh
# 1/20/24
# Symbolically calculate integrations and symbolically solve derivatives and integrals (anti-derivatives)
import os
import sys
import multiprocessing
import sympy as sp
import string
from menu_print_options import *
from custom_exceptions import _MatchBreak


def sanitize_for_sympify(input_string):
    # Define a whitelist of allowed symbols and operators
    allowed_symbols = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.+-*/()^')

    # Filter out any characters not in the whitelist
    sanitized_string = ''.join(char for char in input_string if char in allowed_symbols)

    return sanitized_string


def get_cpu_core_count():
    try:
        # On Linux and macOS
        if os.name == 'posix':
            return os.sysconf('SC_NPROCESSORS_ONLN')

        # On Windows
        elif os.name == 'nt':
            return multiprocessing.cpu_count()

        # Default fallback
        else:
            return 4  # Unable to determine, assume at least 1 core

    except Exception as e:
        print(f"Error while getting CPU core count: {e}")
        return 4  # Fallback to 1 core in case of an error


if __name__ == '__main__':
    hyper_threading = False
    core_count = get_cpu_core_count()
    if len(sys.argv) > 1 and sys.argv[1] == "--h":
        num_thread = core_count-1 * 2
    else:
        num_thread = core_count

    print("\nIf you're new to Python Look at Library I explain some of the operators")
    option = print_menu()
    while option.isnumeric():
        try:
            match int(option):
                case 1:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    x_square_count = get_numerical_input('Enter number of dx squares: ')
                    x_start = get_string_input("Enter starting point for x: ")
                    x_end = get_string_input("Enter ending point for x: ")
                    function = get_string_input("Enter function (to find length of line enter 1): ")
                    try:
                        solution = sp.integrate(sp.parse_expr(function), (sp.symbols('x'), x_start, x_end))
                        if solution.is_Float:
                            solution = format(solution, ".5f")
                        else:
                            solution = sp.simplify(solution)
                        print(solution)
                    except sp.SympifyError:
                        print("invalid expression provided")
                    except ValueError:
                        print("invalid expression provided")
                    except SyntaxError:
                        print("invalid expression provided")
                case 2:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    print("case: ", 2)
                case 3:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    print("case: ", 3)
                case 4:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    print("case: ", 4)
                case 5:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    print("case: ", 5)
                case 6:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    print("case: ", 6)
                case 7:
                    break
                case _:
                    print("that is not an option :)")
                    break
        except _MatchBreak:
            print("Going back to main menu...")
        option = print_menu()
    print("ending program. Thank you!")
