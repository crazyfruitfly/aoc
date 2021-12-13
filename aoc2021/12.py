import pprint

pp = pprint.PrettyPrinter(indent = 4)

def readup(fn):
    lines = {}
    with open(fn, 'r') as f:
        for l in f.readlines():
            f, t = l.strip().split('-')

            if t != 'start':
                if f in lines:
                    lines[f].append(t)
                else:
                    lines[f]=[t]

            if f != 'start':
                if t in lines:
                    lines[t].append(f)
                else:
                    lines[t]=[f]
    del lines['end']
    return lines


def f_1(lines,routes):
    added = 0
    new_routes = []
    for route in routes:
        if route[-1] != 'end':
            for a in lines[route[-1]]:
                if not (all([x.islower() for x in a]) and a in route):
                    to_append = route.copy()
                    to_append.append(a)
                    new_routes.append(to_append)
                    added += 1
        else:
            new_routes.append(route)
    #pp.pprint(new_routes)
    #input()
    if added > 0:
        return f_1(lines, new_routes)
    else:
        return new_routes


def check_to_add(route, ni):
    if ni == ['start', 'end']:
        return False
    if all([x.islower() for x in ni]):
        if ni not in route:
            return True
        else:
            if any([route.count(x) > 1 for x in route if all([y.islower() for y in x])]):
                return False
            else:
                return True
    else:
        return True


def f_2(lines, routes):
    added = 0
    new_routes = []
    for route in routes:
        if route[-1] != 'end':
            for a in lines[route[-1]]:
                if check_to_add(route, a):
                    to_append = route.copy()
                    to_append.append(a)
                    new_routes.append(to_append)
                    added += 1
        else:
            new_routes.append(route)
    if added > 0:
        return f_2(lines, new_routes)
    else:
        return new_routes


lines = readup('12.in')
r = f_1(lines, [['start']])
pp.pprint(len(r))
r2 = f_2(lines, [['start']])
pp.pprint(len(r2))