__all__ = ["factorize", "attack"]
from patsac.libraries import is_square, isqrt
from patsac.rsa.basic import decrypt


def factorize(n):
    """Fermat factorization
    https://en.wikipedia.org/wiki/Fermat%27s_factorization_method#Basic_method
    """
    a = isqrt(n)
    bb = pow(a, 2) - n
    while not is_square(bb):
        bb += 2 * a + 1
        a += 1
    b = isqrt(bb)
    p, q = int(a + b), int(a - b)
    assert n == p * q
    return int(p), int(q)


def attack(c, e, n):
    """Fermat attack"""
    p, q = factorize(n)
    return decrypt(c, e, (p, q))
