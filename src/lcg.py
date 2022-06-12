__all__ = ['LCG']

from patsac import gcdext, gcd, reduce, invert


# reference : https://github.com/Macmod/lcgcrack

def _crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment


def _crack_unknown_multiplier(states, modulus):
    a = (states[2] - states[1])
    inv = int(invert(states[1]-states[0] % modulus, modulus))
    return _crack_unknown_increment(states, modulus, (a * inv) % modulus)


def _crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(lambda x, y: gcd(x, y), zeroes))
    return _crack_unknown_multiplier(states, modulus)


class LCG:
    def __init__(self, seed=None, multiplier=None,
                 increment=None, modulus=None):
        self.state = seed
        self.m = multiplier
        self.c = increment
        self.n = modulus

    def now(self):
        """ Returns current state """
        return self.state

    def next(self):
        """ Process and return next state """
        self.state = (self.state * self.m + self.c) % self.n
        return self.state

    def prev(self):
        """ Process and return previous state """
        m_inv = int(gcdext(self.m, self.n)[1])
        self.state = (m_inv * (self.state - self.c) % self.n)
        return self.state

    def crack(self, seq):
        """ Cracks LCG from at least 6 known states """
        self.n, self.m, self.c = _crack_unknown_modulus(seq)
        self.state = seq[-1]
        return self.n, self.m, self.c
