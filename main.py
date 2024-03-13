# Caige Middaugh
# 1/20/24
# Symbolically calculate integrations and symbolically solve derivatives and integrals (anti-derivatives)
import os
import sys
import multiprocessing
from Integrals import DoubleIntegration
from Integrals import SingleIntegration
from InputOutputOperations.menu_print_options import *
from InputOutputOperations.main_menu import MainMenu
from Integrals.Integral import Integral
from Integrals.SingleIntegration import SingleIntegrationCalculator
from shared.custom_exceptions import MatchBreak
import shared.constants as const


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
    global num_threads
    if len(sys.argv) > 1 and sys.argv[1] == "--h":
        num_threads = core_count//3
    else:
        num_threads = core_count//2
    print("thread count: ", num_threads)
    while main_menu.display_menu().isnumeric():
        try:
            match int(main_menu.options):
                case 1:
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    x_inputs = get_integral_inputs('x')
                    x_inputs[const.FUNCTION] = get_function(['x'])
                    match get_integral_options():
                        case 1:
                            x_inputs[const.TOTAL_SQUARES] = get_numerical_input('Enter number of dx squares: ', integer=True)
                            single_integration_calculator = SingleIntegrationCalculator(
                                Integral('x', x_inputs, is_riemann=True), x_inputs[const.FUNCTION])
                            single_integration_calculator.calculate_integral(num_threads, x_inputs)
                        case _:
                            single_integration_calculator = SingleIntegrationCalculator(
                                Integral('x', x_inputs), x_inputs[const.FUNCTION])
                            single_integration_calculator.solve_integral()
                # case 2:
                    # print("\ninput E, Exit, or Break to go back to previous menu")
                    # match get_integral_options():
                    #     case 1:
                    #         inputs = {'x': get_integral_inputs('x', numerical_inputs=True),
                    #                   'y': get_integral_inputs('y', numerical_inputs=True),
                    #                   const.FUNCTION: get_function(['x', 'y'])}
                    #         inputs['x'][const.TOTAL_SQUARES] = get_numerical_input("Number of dx squares: ", integer=True)
                    #         inputs['y'][const.TOTAL_SQUARES] = get_numerical_input("Number of dy squares: ", integer=True)
                    #         doubleIntegrationCalculator = double_integration.DoubleIntegrationCalculator(inputs, is_riemann=True)
                    #         doubleIntegrationCalculator.calculate_integral(num_threads)
                    #     case _:
                    #         inputs = {'x': get_integral_inputs('x'),
                    #                   'y': get_integral_inputs('y'),
                    #                   const.FUNCTION: get_function(['x', 'y'])}
                    #         doubleIntegrationCalculator = double_integration.DoubleIntegrationCalculator(inputs)
                    #         doubleIntegrationCalculator.solve_integral()
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
                    print("\ninput E, Exit, or Break to go back to previous menu")
                    print("case: ", 7)
                case 8:
                    break
                case _:
                    print("that is not an option :)")
                    break
        except MatchBreak:
            print("Going back to main menu...")
    print("ending program. Thank you!")
