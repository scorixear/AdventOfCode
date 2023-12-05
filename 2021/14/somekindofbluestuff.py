from math import ceil
import os, sys
def main(steps):
    pair_to_elem = dict()
    pairs = dict()
    elements = dict()
    template = ""
    with open(os.path.join(sys.path[0], 'input'), 'r') as file:
        while line := file.readline():
            if line != "\n":
                if len(line.split()) < 3:
                    template = line[:-1]
                else:
                    # print(line[:-1].split())
                    pair_to_elem.update({line[:-1].split()[0]: line[:-1].split()[2]})
                    pairs.update({line[:-1].split()[0]: 0})
                    elements.update({line[:-1].split()[2]: 0})

    for key in range(len(template)-1):
        temp = "".join(template[key:key+2])
        for p in pairs.keys():
            if temp == p:
                pairs.update({temp: pairs[temp]+1})

    for _ in range(steps):
        pairs = step(pairs, pair_to_elem)

    count(pairs, elements)
    print(max(elements.values()) - min(elements.values()))

def count(pairs, elements):
    for e in elements:
        for key, value in zip(pairs.keys(), pairs.values()):
            if e in key:
                elements[e] += key.count(e)*value
        elements[e] = ceil(elements[e]/2)

def step(pairs, pair_to_elem):
    temp = {key: 0 for key in pairs}
    for key, value in zip(pairs.keys(), pairs.values()):
        if value != 0:
            if key in pair_to_elem:
                pair = key[0] + pair_to_elem[key]
                pair2 = pair_to_elem[key] + key[1]
                if pair in pairs:
                    temp[pair] += 1*value
                if pair2 in pairs:
                    temp[pair2] += 1*value
    return temp
main(10)