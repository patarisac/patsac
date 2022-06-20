# patsac
`patsac` is a Python toolkit that I created to help me solve cryptography CTF challenges. `patsac` is still in development and not well-written yet.

## Requirements
- [pwntools](https://github.com/Gallopsled/pwntools)
- [pycryptodome](https://github.com/Legrandin/pycryptodome)
- [libnum](https://github.com/hellman/libnum)
- [gmpy2](https://github.com/aleaxit/gmpy)

## Installation
### Make sure that you have Python 3.8.x
```bash
python3 --version
```
### Clone the repo
```bash
git clone https://github.com/patarisac/patsac.git
```
### Install the requirements
```bash
python3 -m pip install -r requirements.txt
```
### Run `install.sh`
```bash
./install.sh
```

## Example usage
```python
>>> from patsac import *
>>> n = 99407569212588161532909547486944244848185101486332777428538422741011884594253
>>> e = 65537
>>> c = 78974565643224754877770524051794297924332153266350749186075781326292672588454
>>> m = rsa.fermat.attack(c,e,n)
>>> n2s(m)
b'flag{just_a_sample_flag}'
>>> 
```
```python
>>> from patsac.lcg import LCG
>>> known_states = [2818206783446335158, 3026581076925130250,
...                 136214319011561377, 359019108775045580,
...                 2386075359657550866, 1705259547463444505]
>>> rng = LCG()
>>> rng.crack(known_states)
(4611686018427387847, 302080878814014441, 3613230612905734352)
>>> (rng.n, rng.m, rng.c)
(4611686018427387847, 302080878814014441, 3613230612905734352)
>>> 
```
