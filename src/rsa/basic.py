__all__ = ["get_private", "encrypt", "decrypt"]
from patsac.libraries import invert


def get_private(e=0, factors=()):
    """Returns private exponent (d) and modulo (n)"""
    n = 1
    phi = 1
    for f in factors:
        n *= f
        phi *= f - 1
    d = invert(e, phi)
    return int(d), int(n)


def encrypt(m, e, n):
    """Returns ciphertext (c)"""
    return pow(m, e, n)


def decrypt(c=0, e=0, factors=()):
    """Returns plaintext (m)"""
    d, n = get_private(e, factors)
    m = pow(c, d, n)
    return int(m)
