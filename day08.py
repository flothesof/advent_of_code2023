import re

test_input1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_input2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# inp = test_input2
inp = open('data/input08').read()

lr_instrs = inp.split('\n\n')[0].strip()
mapping = {}
for line in inp.split('\n\n')[1].split('\n'):
    key, l, r = re.findall('(\w+)', line)
    mapping[key] = (l, r)

pos = 'AAA'

steps = 0
while not pos == 'ZZZ':
    pos = mapping[pos][{'L': 0, 'R': 1}[lr_instrs[steps % len(lr_instrs)]]]
    steps += 1

steps
###############################################################################
from functools import lru_cache

test_input3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

# inp = test_input3
inp = open('data/input08').read()

lr_instrs = inp.split('\n\n')[0].strip()
mapping = {}
for line in inp.split('\n\n')[1].split('\n'):
    key, l, r = re.findall('(\w+)', line)
    mapping[key] = (l, r)

@lru_cache(maxsize=None)
def move(pos, lr):
    lr = {'L': 0, 'R': 1}[lr]
    return tuple(mapping[p][lr] for p in pos)

@lru_cache(maxsize=None)
def single_move(p, lr):
    lr = {'L': 0, 'R': 1}[lr]
    return mapping[p][lr]

pos = tuple(key for key in mapping if key.endswith('A'))
print(pos)

endpos = [key for key in mapping if key.endswith('Z')]
e = [endpos[0]]
for _ in range(10):
    ancestors = {key: vals for key, vals in mapping.items() if any(ee in vals for ee in e)}
    ancestor = list(ancestors.keys())
    print(f"if I want to end up on {e}, I need to come from {ancestor}")
    e = ancestor

###############################################################################
for p in pos:
    print(p)

    steps = 0
    while not p.endswith('Z'):
        pos = single_move(p, lr_instrs[steps % len(lr_instrs)])
        steps += 1
        if steps % 100000 == 0: print(steps)

    print(steps)

print('part2:', steps)
###############################################################################

