import pprint

pp = pprint.PrettyPrinter(indent = 4)

def readup(fn):
    graph = {}
    with open(fn, 'r') as f:
        for l in f.readlines():
            ft = l.strip().split(' = ')[0].split()
            f, t = ft[0], ft[-1]
            d = int(l.strip().split(' = ')[-1])
            if f in graph:
                graph[f].append( {t: d} )
            else:
                graph[f] = [{t: d}]
            if t in graph:
                graph[t].append( {f: d} )
            else:
                graph[t] = [{f: d}]
    return graph

def init_routes(graph):
    return [[x] for x in graph.keys()]

def generate_routes(routes, graph):
    new_routes = []
    changed = 0
    for route in routes:
        for i in graph[route[-1]]:
            for dest in i.keys():
                if dest not in route:
                    new_route = route.copy()
                    new_route.append(dest)
                    changed += 1
                    new_routes.append(new_route)
    if changed > 0:
        return generate_routes(new_routes, graph)
    else:
        return routes

def calc(routes, graph):
    d = []
    for route in routes:
        dist = 0
        for i in range(len(route)-1):
            for item in graph[route[i]]:
                if route[i+1] in item:
                    dist += item[route[i+1]]
        d.append(dist)
    print(min(d))
    print(max(d))

graph = readup('9.in')
routes = init_routes(graph)
routes = generate_routes(routes, graph)
pp.pprint(routes)
calc(routes, graph)