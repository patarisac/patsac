from .libraries import invert, getPrime, gcdext, iroot


def encrypt(m, e, n):
    c = pow(m, e, n)
    return c


def decrypt(c=0, e=0, factors=()):
    n = 1
    phi = 1
    for f in factors:
        n *= f
        phi *= f - 1
    d = invert(e, phi)
    m = pow(c, d, n)
    return m


def simple_commod_attack(c=[], e=[], n=0):
    """Simple common modulus attack"""
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
