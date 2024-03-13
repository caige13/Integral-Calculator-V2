import sympy as sp
import multiprocessing
import shared.constants as const
from Integrals.Integral import Integral


class BaseIntegration():
    def __init__(self, integrals: [Integral], function: sp.Expr):
        self.integrals = integrals
        self.function = function

    def solve_integral(self):
        answer = self.function
        for integral in self.integrals:
            answer = integral.integrate(answer)
        print("Result of the double integral: ", answer)

    def calculate_riemann_sum(self, endpoint, start_i, end_i):
        raise NotImplementedError("Subclass must implement abstract method")

    def calculate_riemann_sum_multiprocessing(self, endpoint, start_i, end_i, sums, lock):
        raise NotImplementedError("Subclass must implement abstract method")

    def calculate_integral(self, num_processes):
        raise NotImplementedError("Subclass must implement abstract method")