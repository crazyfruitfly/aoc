import pprint
import numpy as np

pp = pprint.PrettyPrinter(indent = 2)

def readup(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
        draws = [int(x) for x in lines[0].strip().split(',')]
        cards = []
        card = None
        for i in range(1,len(lines)):
            if i % 6 == 1:
                if card:
                    cards.append(np.array(card))
                card = []
            else:
                card.append([int(x.strip()) for x in lines[i].split()])
        cards.append(np.array(card))
    return cards, draws


def check_draw(cards, draws):
    for card in cards:
        diag = card.diagonal()
        antidiag = np.fliplr(card).diagonal()
        a = any([all([x in draws for x in row]) for row in card])
        a = a or any([all([x in draws for x in row]) for row in card.transpose()])
        if a:
            return card
    return None


def check_draw_2(cards, draws, indexes):
    num = 0
    for card_index in range(0, len(cards)):
        a = any([all([x in draws for x in row]) for row in cards[card_index]])
        a = a or any([all([x in draws for x in row]) for row in cards[card_index].transpose()])
        if a:
            if card_index not in indexes:
                indexes.append(card_index)
            num += 1
    return num, indexes


def calc(winner, draws):
    s = 0
    for x in winner:
        for y in x:
            s += y if y not in draws else 0
    print(s * draws[-1])


def sim(cards, draws):
    d = []
    winner = None
    for draw in draws:
        d.append(draw)
        winner = check_draw(cards, d)
        if winner is not None:
            break
    calc(winner, d)


def sim_2(cards, draws):
    d = []
    winner = None
    lastnum = 0
    lastdraws = None
    indexes = []
    for draw in draws:
        d.append(draw)
        num, indexes = check_draw_2(cards, d, indexes)
        if num > lastnum:
            lastnum = num
            lastdraws = list(d)
    calc(cards[indexes[-1]], lastdraws)


cards, draws = readup('test4.in')
sim(cards, draws)
sim_2(cards, draws)
print('------------------------------')
cards, draws = readup('4.in')
sim(cards, draws)
sim_2(cards, draws)