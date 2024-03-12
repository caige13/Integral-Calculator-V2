import sympy as sp
import shared.constants as const
import shared.converter as converter


def calculate_riemann_sums(inputs):
    start = inputs[const.START]
    end = inputs[const.END]
    total_squares = inputs[const.TOTAL_SQUARES]
    function = inputs[const.FUNCTION]
    start, end = converter.convert_start_end(start, end)
    delta = (end - start)/total_squares
    left_sum = right_sum = middle_sum = 0
    point = start+delta

    for i in range(0, total_squares):
        left_sum += function.evalf(subs={'x': point-delta})*delta
        right_sum += function.evalf(subs={'x': point})*delta
        middle_sum += (function.evalf(subs={'x': point-delta}) + function.evalf(subs={'x': point}))/2*delta
        point += delta
    print("Left Point Sum: ", format(left_sum, '.5f'))
    print("Right Point Sum: ", format(right_sum, '.5f'))
    print("Mid Point Sum: ", format(middle_sum, '.5f'))


def solve_single_integral(inputs):
    solution = sp.integrate(
        inputs[const.FUNCTION],
        (
            sp.symbols('x'),
            inputs[const.START],
            inputs[const.END]
        )
    )
    if solution.is_Float:
        solution = format(solution, ".5f")
    else:
        solution = sp.simplify(solution)
    print(solution)
