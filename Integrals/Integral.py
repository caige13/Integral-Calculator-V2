import sympy as sp
import shared.constants as const


class Integral:
    def __init__(self, symbol, inputs):
        self.symbol = sp.Symbol(symbol)
        self.start = inputs[const.START]
        self.end = inputs[const.END]

    def integrate(self, function):
        return sp.integrate(function, (self.symbol, self.start, self.end))
