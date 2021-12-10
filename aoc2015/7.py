import numpy as np
import json

AND = lambda x,y: np.uint16(np.bitwise_and(x,y))
OR = lambda x,y: np.uint16(np.bitwise_or(x,y))
LSHIFT = lambda x,y: np.uint16(np.left_shift(x,y))
RSHIFT = lambda x,y: np.uint16(np.right_shift(x,y))
NOT = lambda x: np.uint16(np.invert(x))
nothing = lambda x: np.uint16(x)

gates = {'AND': AND, 'OR': OR, 'LSHIFT': LSHIFT, 'RSHIFT':RSHIFT, 'NOT':NOT, 'nothing': nothing}

def isint(a):
    try:
        return np.uint16(int(a))
    except Exception as e:
        return None

def readup(fn):
    board = {'all_wire': [], 'known_wire': {}, 'board': []}
    with open(fn, 'r') as f:
        for l in f.readlines():
            line = [x.strip() for x in l.split('->')]
            board['all_wire'].append(line[-1])
            if any([x in gates for x in line[0].split()]):
                tmp = line[0].split()
                if 'NOT' in tmp:
                    board['board'].append({'inputs': [tmp[-1]], 'gate': 'NOT', 'output': line[-1]})
                else:
                    board['board'].append({'inputs': [tmp[0], tmp[-1]], 'gate': tmp[1], 'output': line[-1]})
            else:
                if isint(line[0]):
                    board['known_wire'][line[-1]] = np.uint16(int(line[0]))
                else:
                    board['board'].append({'inputs': [line[0]], 'gate': 'nothing', 'output': line[-1]})
    return board

known_wire_num = 0

def sim(board):
    global known_wire_num
    """if len(board['known_wire']) > known_wire_num:
        known_wire_num = len(board['known_wire'])
    else:
        print(board['known_wire'])
        print(board['board'])
        input()"""

    to_delete = []
    index = 0
    for i in board['board']:
        if all([x in board['known_wire'] or isint(x) != None for x in i['inputs']]):
            to_delete.append(index)
            if i['gate'] not in ['NOT', 'nothing']:
                a = board['known_wire'][i['inputs'][0]] if i['inputs'][0] in board['known_wire'] else np.uint16(int(i['inputs'][0]))
                b = board['known_wire'][i['inputs'][1]] if i['inputs'][1] in board['known_wire'] else np.uint16(int(i['inputs'][1]))
                board['known_wire'][i['output']] = gates[i['gate']](a, b)
            else:
                a = board['known_wire'][i['inputs'][0]] if i['inputs'][0] in board['known_wire'] else np.uint16(int(i['inputs'][0]))
                board['known_wire'][i['output']] = gates[i['gate']](a)
        index += 1
    
    for i in sorted(to_delete, reverse=True):
        del board['board'][i]

    if all([x in board['known_wire'] for x in board['all_wire']]):
        return board
    else:
        return sim(board)
 
board = readup('7.in')
board = sim(board)
print(board['known_wire'])

board2 = readup('7.in')
board2['known_wire']['b'] = 3176
board2 = sim(board2)
print(board2['known_wire'])