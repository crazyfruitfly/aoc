target_area = (range(265,288), range(-103,-57))
#target_area = (range(20,31), range(-10,-4))

def shot(iv):
    velocity = [iv]
    coords = [(0,0)]
    while coords[-1][0] <= target_area[0][-1] and coords[-1][1] >= target_area[1][0]:
        if coords[-1][0] in target_area[0] and coords[-1][1] in target_area[1]:
            return True, coords

        nc = (coords[-1][0] + velocity[-1][0], coords[-1][1] + velocity[-1][1])
        nvx, nvy = None, None
        if velocity[-1][0] > 0:
            nvx = velocity[-1][0]-1
        elif velocity[-1][0] < 0:
            nvx = velocity[-1][0]+1
        else:
            nvx = 0 
        nvy = velocity[-1][1]-1
        velocity.append( (nvx, nvy))
        coords.append(nc)
    return False, coords

def f_1():
    hits = []
    for i in range(target_area[0][-1]):
        for j in range(0,150):
            hit, coords = shot((i,j))
            if hit:
                hits.append(coords)
    print(max([y[-1] for x in hits for y in x]))

def f_2():
    hits = []
    for i in range(target_area[0][-1] +1):
        for j in range(-150,150):
            hit, coords = shot((i,j))
            if hit:
                print(i, j)
                hits.append(coords)
    print(len(hits))

#print(30 in target_area[0], -6 in target_area[1])
#print(30 < target_area[0][-1], -6 >= target_area[1][0])
#print(shot((9,0)))
#exit()
#f_1()
f_2()