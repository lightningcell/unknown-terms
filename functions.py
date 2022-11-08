def factoriel(x):
    """ :return x!"""
    counter = 1
    for n in range(1, x + 1):
        counter *= n
    return counter


def permutation(n, r):
    return int(factoriel(n) / factoriel(n - r))


def combination(n, r):
    return int(permutation(n, r) / factoriel(r))
