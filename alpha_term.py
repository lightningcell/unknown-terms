class AlphaTerm:
    def __init__(self, _coe=1, _alpha="x", _exp=1):
        self.__coefficient = _coe
        self.__alpha = _alpha
        self.__exponent = _exp

    def get_coefficient(self) -> int:
        return self.__coefficient

    def get_alpha(self) -> str:
        return self.__alpha

    def get_exponent(self) -> int:
        return self.__exponent

    def get_printable_exponent(self) -> str:
        exponents = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

        if len(str(self.__exponent)) == 1:
            if self.__exponent == 1:
                return ""
            else:
                return exponents[self.__exponent]
        else:
            full_exponent = str()
            for _exp in str(self.__exponent):
                full_exponent += exponents[int(_exp)]
            return full_exponent

    def get_printable_coefficient(self) -> str:
        if self.__coefficient == 1:
            return ""
        else:
            return str(self.__coefficient)

    def get_full_term(self):
        return self.get_printable_coefficient() + self.__alpha + self.get_printable_exponent()

    def __str__(self):
        return self.get_full_term()
