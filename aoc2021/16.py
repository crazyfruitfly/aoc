import pprint, math

pp = pprint.PrettyPrinter(indent=2)
hextob = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def readup(fn):
    binstr = ''
    with open(fn, 'r') as f:
        for i in f.read().strip():
            binstr += hextob[i]
    return binstr


def get_header(binstr):
    return int(binstr[0:3], 2), int(binstr[3:6], 2), binstr[6:]


def get_packets(binstr):
    if all(['0' == x for x in binstr]):
        return binstr, packets
    pversion, ptype, binstr = get_header(binstr)
    
    if ptype == 4:
        f = ''
        while True:
            num = binstr[:5]
            f += num[1:]
            binstr = binstr[5:]
            if num[0] == '0':
                break
        return binstr, {'version': pversion, 'type': ptype, 'literal': int(f, 2), 'subpackets': []}
    else:
        packet = {'version': pversion, 'type': ptype, 'subpackets': []}
        t = binstr[0]
        binstr = binstr[1:]
        if t == '0':
            packetlength = binstr[:15]
            binstr = binstr[15:]
            l = int(packetlength, 2)
            sps = binstr[:l]
            binstr = binstr[l:]
            while not all([x == '0' for x in sps]):
                sps, p = get_packets(sps)
                packet['subpackets'].append(p)
            return binstr, packet
        else:
            packetnum = int(binstr[:11], 2)
            binstr = binstr[11:]
            for _ in range(packetnum):
                binstr, p = get_packets(binstr)
                packet['subpackets'].append(p)
            return binstr, packet


def f_1(a):
    s = a['version']
    if a['subpackets'] == []:
        return s
    else:
        return s + sum(list(map(f_1, a['subpackets'])))

def f_2(a):
    if a['type'] == 4:
        return a['literal']
    elif a['type'] == 0:
        return sum(list(map(f_2, a['subpackets'])))
    elif a['type'] == 1:
        return math.prod(list(map(f_2, a['subpackets'])))
    elif a['type'] == 2:
        return min(list(map(f_2, a['subpackets'])))
    elif a['type'] == 3:
        return max(list(map(f_2, a['subpackets'])))
    elif a['type'] == 5:
        return 1 if f_2(a['subpackets'][0]) > f_2(a['subpackets'][1]) else 0
    elif a['type'] == 6:
        return 1 if f_2(a['subpackets'][0]) < f_2(a['subpackets'][1]) else 0
    elif a['type'] == 7:
        return 1 if f_2(a['subpackets'][0]) == f_2(a['subpackets'][1]) else 0


packets = {'packets': []}
binstr = readup('16.in')    
binstr, a = get_packets(binstr)
#pp.pprint(a)
print(f_1(a))
print(f_2(a))