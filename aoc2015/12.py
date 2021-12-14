import json

def readup(fn):
    with open(fn, 'r') as f:
        return json.loads(f.read())

def get_numbers(item, numbers):
    if isinstance(item,dict):
        #for part two
        for key, value in item.items():
            if value == "red":
                return
        #
        for key, value in item.items():
            get_numbers(value, numbers)
    elif isinstance (item, list):
        for i in item:
            get_numbers(i, numbers)
    elif isinstance(item, int):
        numbers.append(item)
    else:
        numbers.append(0)

o = readup('12.in')
alma = []
get_numbers(o, alma)
print(sum(alma))