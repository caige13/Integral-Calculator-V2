import sympy as sp
import multiprocessing
import shared.constants as const
from sympy.integrals import integrate

from Integrals.Interfaces.BaseIntegration import BaseIntegration


class DoubleIntegrationCalculator(BaseIntegration):
    def calculate_riemann_sum(self, endpoint, start_i, end_i):
        total_sum = 0
        for i in range(start_i, end_i):
            for j in range(self.num_rectangles_y):
                x_val = self.start_x + i * self.delta_x
                y_val = self.start_y + j * self.delta_y

                match endpoint:
                    case 'upper_left':
                        total_sum += self.function.subs({self.x: x_val, self.y: y_val}) * self.delta_area
                    case 'upper_right':
                        total_sum += self.function.subs({self.x: x_val + self.delta_x, self.y: y_val}) * self.delta_area
                    case 'lower_left':
                        total_sum += self.function.subs({self.x: x_val, self.y: y_val + self.delta_y}) * self.delta_area
                    case 'lower_right':
                        total_sum += self.function.subs({self.x: x_val + self.delta_x, self.y: y_val + self.delta_y}) * self.delta_area
                    case 'middle':
                        total_sum += self.function.subs({self.x: (x_val+x_val+self.delta_x)/2, self.y: (y_val+y_val+self.delta_y)/2}) * self.delta_area

        return total_sum

    def calculate_riemann_sum_multiprocessing(self, endpoint, start_i, end_i, sums, lock):
        local_sum = self.calculate_riemann_sum(endpoint, start_i, end_i)

        with lock:
            sums[endpoint].value += local_sum

    def calculate_integral(self, num_processes, inputs):
        self.num_rectangles_x = inputs['x'][const.TOTAL_SQUARES]
        self.num_rectangles_y = inputs['y'][const.TOTAL_SQUARES]
        self.delta_x = (self.end_x - self.start_x) / self.num_rectangles_x
        self.delta_y = (self.end_y - self.start_y) / self.num_rectangles_y
        self.delta_area = self.delta_x * self.delta_y
        endpoints = ['upper_left', 'upper_right', 'lower_left', 'lower_right', 'middle']
        sums = {endpoint: multiprocessing.Value('d', 0.0) for endpoint in endpoints}
        lock = multiprocessing.Lock()

        processes = []
        rectangles_per_process = self.num_rectangles_x // num_processes
        for endpoint in endpoints:
            for i in range(num_processes):
                start_i = i * rectangles_per_process
                if i < num_processes - 1:
                    end_i = start_i + rectangles_per_process
                else:
                    end_i = self.num_rectangles_x
                process = multiprocessing.Process(
                    target=self.calculate_riemann_sum_multiprocessing,
                    args=(endpoint, start_i, end_i, sums, lock)
                )
                processes.append(process)
                process.start()
            for process in processes:
                process.join()
            print("For ", endpoint, " sum was: ", sums[endpoint].value)
