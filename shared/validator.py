import sympy as sp


def has_symbol(symbol, expression):
    symbol = sp.Symbol(symbol)
    return expression.has(symbol)


def has_multiple_symbols(symbols, expression):
    for symbol in symbols:
        if not has_symbol(symbol, expression):
            return False
    return True
