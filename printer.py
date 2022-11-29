class TermPrinter:
    @staticmethod
    def print(any_term, with_sign=False, sign_space=1):
        if type(any_term) in [float, int]:
            return TermPrinter.get_printable_coefficient(any_term)

        sign = ""
        if with_sign:
            if any_term.get_coefficient() < 0:
                sign = (" " * sign_space) + "-" + (" " * sign_space)
            elif any_term.get_coefficient() > 0:
                sign = (" " * sign_space) + "+" + (" " * sign_space)

            any_term = abs(any_term)  # The sign will be add already

        if hasattr(any_term, "terms"):
            return sign + TermPrinter.__print_multiple_alpha_term(any_term)
        elif hasattr(any_term, "is_equal_zero"):
            return sign + TermPrinter.__print_alpha_term(any_term)
        else:
            raise ValueError("The any_term parameter must be an actionable value.")

    @staticmethod
    def __print_alpha_term(term):
        if term.get_coefficient() == 0:
            return ""
        elif term.get_exponent() == 0:
            return term.get_printable_coefficient()
        elif term.get_exponent != 0:
            if term.get_coefficient() == 1:
                return term.get_alpha() + TermPrinter.get_printable_exponent(term.get_exponent())
            else:
                return (term.get_printable_coefficient()
                        + term.get_alpha()
                        + TermPrinter.get_printable_exponent(term.get_exponent()))

    @staticmethod
    def __print_multiple_alpha_term(multiple_term):
        if multiple_term.get_coefficient() == 0:
            return ""
        else:
            coefficient = multiple_term.get_coefficient()
            alp_exp = ""
            for term in multiple_term.seperated_terms:
                term.set_coefficient(1)
                obj = TermPrinter.__print_alpha_term(term)
                if not obj.isnumeric():
                    alp_exp += obj

            if len(alp_exp) == 0:
                return TermPrinter.get_printable_coefficient(coefficient)
            else:
                pr_coe = ""
                if coefficient != 1:
                    pr_coe = TermPrinter.get_printable_coefficient(coefficient)

                return pr_coe + alp_exp

    @staticmethod
    def get_printable_coefficient(_coe):
        return str(int(_coe)) if float(_coe).is_integer() else str(_coe)

    @staticmethod
    def get_printable_exponent(_exp, is_regular=True):
        if _exp in [0, 1] and is_regular:
            return ""

        minus = "⁻"
        if _exp == -1 and is_regular:
            return minus

        exponents = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        abs_exponent = abs(_exp)
        result = minus if _exp < 0 else ""

        for i in str(abs_exponent):
            result += exponents[int(i)]
        return result
