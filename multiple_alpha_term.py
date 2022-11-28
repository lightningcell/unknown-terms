class MultipleAlphaTerm:
    def __init__(self, _terms, _add_coefficient=1.0):
        self.terms = _terms
        self.add_coefficient = _add_coefficient
        self.__coefficient = 1.0 * _add_coefficient
        self.seperated_terms = self.seperate_by_alphas()

    def get_coefficient(self):
        return self.__coefficient

    @staticmethod
    def __multiply_alpha_bros(terms) -> 'AlphaTerm':
        result = 1
        for term in terms:
            result *= term
        return result

    def seperate_by_alphas(self) -> list:
        terms_dict = dict()
        for _term in self.terms:
            if not terms_dict.get(_term.get_alpha()):
                terms_dict[_term.get_alpha()] = list()
            terms_dict[_term.get_alpha()].append(_term)

        for alpha in terms_dict.keys():
            if len(terms_dict[alpha]) > 1:
                terms_dict[alpha] = [self.__multiply_alpha_bros(terms_dict[alpha])]

        final_terms = []
        for t in terms_dict.values():
            final_terms.append(t[0])
            self.__coefficient *= t[0].get_coefficient()
        return final_terms

    def get_full_term(self) -> str:
        alpha_exp = ""

        for term in self.seperated_terms:
            alpha_exp += term.get_alpha() + term.get_printable_exponent()

        return str(self.get_coefficient()) + alpha_exp

    def turn_to_known(self, **values) -> float:
        result = 1
        for term in self.seperated_terms:
            result *= term.turn_to_known(values[term.get_alpha()])

        return result

    def __str__(self) -> str:
        return self.get_full_term()

    def __mul__(self, other) -> 'MultipleAlphaTerm':
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
        if type(other) in [int, float]:
            if other == 0:
                raise ValueError("MultipleAlphaTerm object cannot be divided by zero")
            return self.__mul__(1 / other)
        elif isinstance(other, type(self.terms[-1])):
            if other.is_equal_zero:
                raise ValueError("MultipleAlphaTerm object cannot be divided by zero")
            else:
                new_object = other.__copy__()
                new_object.set_coefficient(1 / other.get_coefficient())
                new_object.set_exponent(-other.get_exponent())
            return MultipleAlphaTerm(self.terms + [new_object])
        elif isinstance(other, type(self)):
            other_terms = []
            for term in other.terms:
                new_term = term.__copy__()
                new_term.set_coefficient(1 / term.get_coefficient())
                new_term.set_exponent(-term.get_exponent)
                other_terms.append(new_term)

            return MultipleAlphaTerm(self.terms + [other_terms])

    def __float__(self):
        return float(self.__coefficient)

    def __abs__(self):
        new_term = MultipleAlphaTerm(self.terms, self.add_coefficient)
        new_term.__coefficient = abs(new_term.get_coefficient())
        new_term.add_coefficient = abs(new_term.add_coefficient)
        return new_term
