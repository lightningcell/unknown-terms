class MultipleAlphaTerm:
    def __init__(self, _terms, _add_coefficient=1.0):
        self.terms = _terms
        self.add_coefficient = _add_coefficient
        self.coefficient = 1.0 * _add_coefficient
        self.seperated_terms = self.seperate_by_alphas()

    @staticmethod
    def __multiply_alpha_bros(terms):
        result = 1
        for term in terms:
            result *= term
        return result

    def seperate_by_alphas(self):
        terms_dict = dict()
        for _term in self.terms:
            if _term.is_equal_one:
                continue
            if not terms_dict.get(_term.get_alpha()):
                terms_dict[_term.get_alpha()] = list()
            terms_dict[_term.get_alpha()].append(_term)

        for alpha in terms_dict.keys():
            if len(terms_dict[alpha]) > 1:
                terms_dict[alpha] = [self.__multiply_alpha_bros(terms_dict[alpha])]

        final_terms = []
        for t in terms_dict.values():
            final_terms.append(t[0])
            self.coefficient *= t[0].get_coefficient()

        return final_terms

    def get_full_term(self):
        alpha_exp = ""

        for term in self.seperated_terms:
            if term.is_equal_zero:
                return "0"
            if term.is_equal_one:
                continue
            alpha_exp += term.get_alpha() + term.get_printable_exponent()

        if self.coefficient.is_integer():
            self.coefficient = int(self.coefficient)

        return str(self.coefficient) + alpha_exp

    def __str__(self):
        return self.get_full_term()

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return MultipleAlphaTerm(self.terms, _add_coefficient=other * self.add_coefficient)
        elif isinstance(other, type(self.terms[-1])):  # self.terms[-1] always will be an AlphaTerm object.
            new_terms = self.terms + [other]
            return MultipleAlphaTerm(new_terms, self.add_coefficient)
        elif isinstance(other, type(self)):
            new_terms = self.terms + other.terms
            return MultipleAlphaTerm(new_terms, self.add_coefficient)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, power):
        new_terms = []
        for term in self.seperated_terms:
            new_terms.append(term ** power)

        return MultipleAlphaTerm(new_terms, self.add_coefficient ** power)

    def __truediv__(self, other):
        return self.__mul__(1 / other)
