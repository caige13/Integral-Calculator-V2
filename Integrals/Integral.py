import sympy as sp
import shared.constants as const


class Integral:
    def __init__(self, symbol, inputs, is_riemann=False):
        self.symbol = sp.Symbol(symbol)
        self.start = inputs[const.START]
        self.end = inputs[const.END]
        if is_riemann:
            self.num_rectangles = inputs[const.TOTAL_SQUARES]
            self.delta = (self.end - self.start) / self.num_rectangles

    def integrate(self, function):
        return sp.integrate(function, (self.symbol, self.start, self.end))

    def get_square_area(self, point_value):
        """
        used for when calculating riemann sums

        point_value: the coordinate point to append to the start
        symbol_delta: the rate at which each point is adjusted by (end-start)/rectangle_amount
        """
        return (self.start + point_value) * self.delta
