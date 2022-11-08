from alpha_term import AlphaTerm
from functions import *


def binomial_expansion(_term1: AlphaTerm, _term2: AlphaTerm, exponent: int):
    """ :return (term1 + term2) ^ exponent"""

    equation = ""
    for i in range(0, exponent + 1):
        result_term1 = 1 if exponent - i == 0 else _term1 ** (exponent - i)
        result_term2 = 1 if i == 0 else _term2 ** i
        result = result_term1 * result_term2 * combination(exponent, i)

        equation += (" + " if i != 0 else "") + str(result)

    return equation


term1 = AlphaTerm(1, "x", 1)
term2 = AlphaTerm(1, "y", 1)

print(binomial_expansion(term1, term2, 10))
