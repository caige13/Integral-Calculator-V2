# Caige Middaugh
# 1/20/24
# Symbolically calculate integrations and symbolically solve derivatives and integrals (anti-derivatives)
import os
import sys
import multiprocessing
import sympy as sp
from Integrals import double_integration
from Integrals import single_integration
from InputOutputOperations.menu_print_options import *
from InputOutputOperations.main_menu import MainMenu
from shared.custom_exceptions import MatchBreak
from shared import constants as const


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
            return 4

    except Exception as e:
        print(f"Error while getting CPU core count: {e}")
        return 4


if __name__ == '__main__':
    hyper_threading = False
    core_count = get_cpu_core_count()
    main_menu = MainMenu()
    global num_thread
    if len(sys.argv) > 1 and sys.argv[1] == "--h":
        num_thread = core_count-1 * 2
    else:
        num_thread = core_count
    while main_menu.display_menu().isnumeric():
        complete = False
        try:
            match int(main_menu.options):
                case 1:
                    while not complete:
                        print("\ninput E, Exit, or Break to go back to previous menu")
                        x_inputs = get_integral_inputs('x', get_function=True)
                        try:
                            match get_single_integral_options():
                                case 1:
                                    x_inputs[const.TOTAL_SQUARES] = get_numerical_input('Enter number of dx squares: ', True)
                                    single_integration.calculate_riemann_sums(x_inputs)
                                case _:
                                    single_integration.solve_single_integral(x_inputs)
                            complete = True
                        except sp.SympifyError:
                            print("invalid expression provided")
                        except ValueError:
                            print("invalid expression provided")
                        except SyntaxError:
                            print("invalid expression provided")
                case 2:
                    while not complete:
                        print("\ninput E, Exit, or Break to go back to previous menu")
                        complete = False
                        inputs = {'x': get_integral_inputs('x'),
                                  'y': get_integral_inputs('y', get_function=True)}
                        try:
                            match get_single_integral_options():
                                case 1:
                                    inputs['x'][const.TOTAL_SQUARES] = get_numerical_input("Number of dx squares: ", True)
                                    inputs['y'][const.TOTAL_SQUARES] = get_numerical_input("Number of dy squares", True)
                                    double_integration.calculate_double_riemann(inputs)
                                case _:
                                    double_integration.solve_double_integral(inputs)
                        except sp.SympifyError:
                            print("invalid expression provided")
                        except ValueError:
                            print("invalid expression provided")
                        except SyntaxError:
                            print("invalid expression provided")
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
        except MatchBreak:
            print("Going back to main menu...")
    print("ending program. Thank you!")
