import sympy as sp
import multiprocessing
import shared.constants as const
import shared.converter as converter
from Integrals.Interfaces.BaseIntegration import BaseIntegration


class SingleIntegrationCalculator(BaseIntegration):
    def calculate_riemann_sum(self, endpoint, start_i, end_i):
        total_sum = 0
        delta = self.integrals[0].delta
        point = start_i + delta
        for i in range(start_i, end_i):
            value = self.integrals[0].get_square_area(i)

            match endpoint:
                case 'left':
                    total_sum += self.function.evalf(subs={'x': point-delta})*delta
                case 'right':
                    total_sum += self.function.evalf(subs={'x': point})*delta
                case 'midpoint':
                    total_sum += (self.function.evalf(subs={'x': point-delta}) + self.function.evalf(subs={'x': point}))/2*delta
            point += delta

    def calculate_riemann_sum_multiprocessing(self, endpoint, start_i, end_i, sums, lock):
        local_sum = self.calculate_riemann_sum(endpoint, start_i, end_i)

        with lock:
            sums[endpoint].value += local_sum

    def calculate_integral(self, num_processes, total_squares):
        num_rectangles = total_squares[const.TOTAL_SQUARES]
        endpoints = ['left', 'right', 'midpoint']
        sums = {endpoint: multiprocessing.Value('d', 0.0) for endpoint in endpoints}
        lock = multiprocessing.Lock()

        processes = []
        rectangles_per_process = num_rectangles // num_processes
        for endpoint in endpoints:
            for i in range(num_processes):
                start_i = i * rectangles_per_process
                if i < num_processes - 1:
                    end_i = start_i + rectangles_per_process
                else:
                    end_i = num_rectangles
                process = multiprocessing.Process(
                    target=self.calculate_riemann_sum_multiprocessing,
                    args = (endpoint, start_i, end_i, sums, lock)
                )
                processes.append(process)
                process.start()
            for process in processes:
                process.join()
            print("For ", endpoint, " sum was: ", sums[endpoint].value)

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
