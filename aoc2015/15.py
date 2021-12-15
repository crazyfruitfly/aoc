import pprint

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    ingredients = {}
    with open(fn, 'r') as f:
        for l in f.readlines():
            what = l.split(':')[0]
            cap, dur, fla, tex, cal = [int(x.split()[-1].strip()) for x in l.split(':')[1].strip().split(',')]
            ingredients[what] = {'cap': cap, 'dur': dur, 'fla': fla, 'tex':tex, 'cal': cal}
    return ingredients

def generate_ratio():
    for i in range(0, 101):
        for j in range(0, 101-i):
            for k in range(0, 101-i-j):
                yield (i,j,k,100-i-j-k)           

def calc(i):
    scores = []
    for ratio in generate_ratio():
        cap = ratio[0]*i['Sugar']['cap'] + ratio[1] *i['Sprinkles']['cap'] + ratio[2] *i['Candy']['cap'] + ratio[3]*i['Chocolate']['cap']
        dur = ratio[0]*i['Sugar']['dur'] + ratio[1] *i['Sprinkles']['dur'] + ratio[2] *i['Candy']['dur'] + ratio[3]*i['Chocolate']['dur']
        fla = ratio[0]*i['Sugar']['fla'] + ratio[1] *i['Sprinkles']['fla'] + ratio[2] *i['Candy']['fla'] + ratio[3]*i['Chocolate']['fla']
        tex = ratio[0]*i['Sugar']['tex'] + ratio[1] *i['Sprinkles']['tex'] + ratio[2] *i['Candy']['tex'] + ratio[3]*i['Chocolate']['tex']
        cal = ratio[0]*i['Sugar']['cal'] + ratio[1] *i['Sprinkles']['cal'] + ratio[2] *i['Candy']['cal'] + ratio[3]*i['Chocolate']['cal']
        cap = 0 if cap < 0 else cap
        dur = 0 if dur < 0 else dur
        fla = 0 if fla < 0 else fla
        tex = 0 if tex < 0 else tex
        score = cap*dur*fla*tex
        scores.append(score)
    print(max(scores))

def calc2(i):
    scores = []
    for ratio in generate_ratio():
        cap = ratio[0]*i['Sugar']['cap'] + ratio[1] *i['Sprinkles']['cap'] + ratio[2] *i['Candy']['cap'] + ratio[3]*i['Chocolate']['cap']
        dur = ratio[0]*i['Sugar']['dur'] + ratio[1] *i['Sprinkles']['dur'] + ratio[2] *i['Candy']['dur'] + ratio[3]*i['Chocolate']['dur']
        fla = ratio[0]*i['Sugar']['fla'] + ratio[1] *i['Sprinkles']['fla'] + ratio[2] *i['Candy']['fla'] + ratio[3]*i['Chocolate']['fla']
        tex = ratio[0]*i['Sugar']['tex'] + ratio[1] *i['Sprinkles']['tex'] + ratio[2] *i['Candy']['tex'] + ratio[3]*i['Chocolate']['tex']
        cal = ratio[0]*i['Sugar']['cal'] + ratio[1] *i['Sprinkles']['cal'] + ratio[2] *i['Candy']['cal'] + ratio[3]*i['Chocolate']['cal']
        cap = 0 if cap < 0 else cap
        dur = 0 if dur < 0 else dur
        fla = 0 if fla < 0 else fla
        tex = 0 if tex < 0 else tex
        score = cap*dur*fla*tex
        if cal == 500:
            scores.append(score)
    print(max(scores))

i = readup('15.in')
calc(i)
calc2(i)