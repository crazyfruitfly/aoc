def readup(fn):
    with open(fn, 'r') as f:
        return f.read().strip()

def step(inp):
    ni = ''
    i = 0
    counter = 1
    for i in range(len(inp)):
        if i + 1 >= len(inp) or inp[i] != inp[i+1]:
            ni += str(counter) + str(inp[i])
            counter = 1
        else:
            counter += 1
    return ni

i = readup('10.in')
for _ in range(50):
    i = step(i)

print(len(i))