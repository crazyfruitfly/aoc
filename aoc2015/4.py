import numpy as np
import hashlib

def readup(fn):
    with open(fn, 'r') as f:
        return f.read().strip()

def f_1(key):
    pf = 1
    while True:
        tohash = key + str(pf)
        h = hashlib.md5(tohash.encode('utf-8'))
        if h.hexdigest().startswith('000000'):
            print(pf)
            break
        pf += 1

key = readup('4.in')
f_1(key)
