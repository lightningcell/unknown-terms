class TermPrinter:
    @staticmethod
    def print(any_term, with_sign=False, sign_space=1):
        sign = ""
        if with_sign:
            if any_term.get_coefficient() < 0:
                sign = "-" + (" " * sign_space)
            elif any_term.get_coefficient() > 0:
                sign = "+" + (" " * sign_space)

        if any_term.__getattribute__("terms"):
            return sign + TermPrinter.__print_multiple_alpha_term(any_term)
        else:
            return sign + TermPrinter.__print_alpha_term(any_term)

    @staticmethod
    def __print_alpha_term(term):
        if term.get_coefficient() == 0:
            return ""
        elif term.get_exponent() == 0:
            return term.get_printable_coefficient()
        else:
            return term.get_full_term()

    @staticmethod
    def __print_multiple_alpha_term(multiple_term):
        if multiple_term.get_coefficient() == 0:
            return ""
        else:
            printable_term = str(multiple_term.get_printable_coefficient())
            for term in multiple_term.seperated_terms:
                alp_exp = TermPrinter.__print_alpha_term(term)[len(str(term.get_printable_coefficient())):]
                printable_term += alp_exp
            return printable_term
