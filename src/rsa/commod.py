__all__ = ["attack"]
from patsac.libraries import gcdext, invert, iroot


def attack(c=[], e=[], n=0):
    """Common modulus attack"""
    g, x, y = gcdext(e[0], e[1])
    if x < 0:
        c[0] = invert(c[0], n)
        x *= -1
    if y < 0:
        c[1] = invert(c[1], n)
        y *= -1
    c[0] = pow(c[0], x, n)
    c[1] = pow(c[1], y, n)
    m = int(c[0] * c[1]) % n
    if int(g) != 1:
        m = int(iroot(m, int(g))[0])
    return m
