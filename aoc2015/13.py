import pprint, itertools

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    a = []
    with open(fn, 'r') as f:
        for l in f.readlines():
            splitted = l.strip().split()
            who = splitted[0]
            next_to = splitted[-1][:-1]
            amount = int(splitted[3]) if 'gain' in l else -1*int(splitted[3])
            a.append({'from': who, 'to': next_to, 'amount': amount})
    return a

def get_happiness(f, t, a):
    for i in a:
        if i['from'] == f and i['to'] == t:
            return i['amount']

def f_1(a):
    delta_happynesses = []
    for s in itertools.permutations(list(set([x['from'] for x in a]))):
        delta_happyness = []
        for i in range(len(s)):
            j = i+1 if i+1 < len(s) else 0
            b = i - 1
            bh = get_happiness(s[i], s[b], a)
            jh = get_happiness(s[i],s[j], a)
            delta_happyness.append( bh + jh)
        delta_happynesses.append(delta_happyness)
    print(max([sum(x) for x in delta_happynesses]))

def f_2(a):
    for i in list(set([x['from'] for x in a])):
        a.append({'from': 'me', 'to': i, 'amount': 0})
        a.append({'from': i, 'to': 'me', 'amount': 0})
    f_1(a)

a = readup('13.in')
f_1(a)
f_2(a)