import numpy as np
import hashlib

vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']
def isnice(word):
    if sum([1 if word[i] == word[i-1] else 0 for i in range(1, len(word))]) > 0:
        if sum([1 if x in vowels else 0 for x in word]) > 2:
            if not any([x in word for x in forbidden]):
                return True
    return False
        

def readup(fn):
    with open(fn, 'r') as f:
        return [l.strip() for l in f.readlines()]

def f_1(words):
    print([isnice(word) for word in words].count(True))

def filter1(word):
    if len(word) < 4:
        return False
    pairs = [word[x:x+2] for x in range(0,len(word)-1)]
    return len([pairs[i] for i in range(0, len(pairs) - 2) if pairs[i + 2:].count(pairs[i]) > 0 ] ) > 0

def filter2(word):
    return len([word[x:x+3] for x in range(0,len(word)-2) if word[x] == word[x+2]]) > 0


def f_2(words):
    #for word in words:
    #    filter1(word)
    first = [word for word in words if filter1(word)]
    print(len([word for word in first if filter2(word)]))

words = readup('5.in')
f_1(words)
f_2(words)