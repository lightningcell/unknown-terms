from .multiple_alpha_term import MultipleAlphaTerm
from .printer import TermPrinter


class AlphaTerm:
    def __init__(self, _coe=1.0, _alpha="x", _exp=1):
        self.__coefficient = float(_coe)
        self.__alpha = _alpha
        self.__exponent = _exp
        self.is_equal_zero = True if self.__coefficient == 0 else False

    def get_coefficient(self) -> float:
        return self.__coefficient

    def get_alpha(self) -> str:
        return self.__alpha

    def get_exponent(self) -> int:
        return self.__exponent

    def get_printable_exponent(self):
        # This function uses TermPrinter but still returns irregular result
        return TermPrinter.get_printable_exponent(self.__exponent, False)

    def get_printable_coefficient(self) -> str:
        # Returns regular coefficient
        return TermPrinter.get_printable_coefficient(self.__coefficient)

    def get_full_term(self) -> str:
        # Irregular term
        return str(self.__coefficient) + self.__alpha + self.get_printable_exponent()

    def set_coefficient(self, _coe: float) -> None:
        self.__coefficient = _coe

    def set_alpha(self, alpha: str) -> None:
        self.__alpha = alpha

    def set_exponent(self, exponent: int):
        self.__exponent = exponent

    def turn_to_known(self, value: float) -> float:
        return self.__coefficient * (value ** self.__exponent)

    def __str__(self):
        return self.get_full_term()

    def __mul__(self, other):
        if type(other) in [float, int]:
            new_coefficient = self.__coefficient * other
            return AlphaTerm(new_coefficient, self.__alpha, self.__exponent)
        elif isinstance(other, type(self)):
            other: AlphaTerm
            if other.get_alpha() == self.__alpha:
                new_coefficient = other.get_coefficient() * self.__coefficient
                new_exponent = other.get_exponent() + self.__exponent
                return AlphaTerm(new_coefficient, self.__alpha, new_exponent)
            else:
                return MultipleAlphaTerm([self, other])
        elif isinstance(other, MultipleAlphaTerm):
            new_terms = other.terms.copy()
            new_terms.extend([self])
            return MultipleAlphaTerm(new_terms)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __copy__(self):
        return AlphaTerm(self.__coefficient, self.__alpha, self.__exponent)

    def __pow__(self, power):
        if isinstance(power, int):
            new_coefficient = self.__coefficient ** power
            new_exponent = self.__exponent * power
            return AlphaTerm(new_coefficient, self.__alpha, new_exponent)
        else:
            raise ValueError("Power had to be an integer")

    def __truediv__(self, other):
        if type(other) in [float, int]:
            if other == 0:
                raise ValueError("AlphaTerm object cannot be divided by zero")
            return self.__mul__(1 / other)
        elif isinstance(other, type(self)):
            if other.is_equal_zero:
                raise ValueError("AlphaTerm object cannot be divided by zero")
            new_term = other.__copy__()
            new_term.set_exponent(-other.get_exponent())
            new_term.set_coefficient(1 / other.get_coefficient())
            return self * new_term
        elif isinstance(other, MultipleAlphaTerm):
            other_terms = []
            for term in other.seperated_terms:
                new_term = term.__copy__()
                new_term.set_exponent(-term.get_exponent())
                new_term.set_coefficient(1 / term.get_coefficient())
                other_terms.append(new_term)

            return MultipleAlphaTerm([self] + other_terms)

    def __float__(self):
        return float(self.coefficient)

    def __abs__(self):
        new_term = self.__copy__()
        new_term.set_coefficient(abs(self.__coefficient))
        return new_term
