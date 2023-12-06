import re

test_input = """Time:      7  15   30
Distance:  9  40  200"""

my_input = """Time:        45     97     72     95
Distance:   305   1062   1110   1695"""

# inp = test_input
inp = my_input

records = list(map(int, re.findall('\d+', inp.splitlines()[0])))
distances = list(map(int, re.findall('\d+', inp.splitlines()[1])))

part1 = 1
for race in range(len(records)):
    record_time = records[race]
    record_distance = distances[race]
    beats = 0
    for t in range(1, record_time):
        remaining_time = record_time - t
        v = t
        dist = v * remaining_time
        if dist > record_distance:
            beats += 1
        # print(t, dist)
    print(beats)
    part1 *= beats

print(f'part1: {part1}')

###############################################################################
# part 2
from tqdm import tqdm

# inp = test_input
inp = my_input

record = int("".join(re.findall('\d+', inp.splitlines()[0])))
distance = int("".join(re.findall('\d+', inp.splitlines()[1])))

record_time = record
record_distance = distance
beats = 0
for t in tqdm(range(1, record_time)):
    remaining_time = record_time - t
    v = t
    dist = v * remaining_time
    if dist > record_distance:
        beats += 1
print(beats)

print(f'part2: {beats}')

###############################################################################
