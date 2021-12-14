import string 
lcl = string.ascii_lowercase

inp = 'hepxcrrq'
inp = 'hepxxyzz'

def rule1(pw):
    return any([s in pw for s in [''.join(y) for y in [x for x in zip(lcl, lcl[1:], lcl[2:])]]])

def rule2(pw):
    return all([x not in ['i','o','l'] for x in pw])

def rule3(pw):
    duos = [''.join(x) for x in zip(lcl, lcl)]
    trios = [''.join(x) for x in zip(lcl, lcl, lcl)]
    c = 0
    for i in range(len(duos)):
        if pw.count(duos[i]) > 2* pw.count(trios[i]):
            c += pw.count(duos[i])
    
    if c >= 2:
        return True
    return False

def calc(pw):
    #i = 0
    while True:
        if rule1(pw) and rule2(pw) and rule3(pw):
            break
        else:
            pw = increase_letter(pw)
        #i += 1

    print(pw)


def increase_letter(inp):
    s = inp[::-1]
    for i in range(len(s)):
        if s[i] == 'z':
            s = s[0:i] + 'a' + s[i+1:]
        else:
            s = s[0:i] + lcl[lcl.index(s[i]) + 1] + s[i+1:]
            break
    return s[::-1]

#for part 2
inp = increase_letter(inp)
calc(inp)