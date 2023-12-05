test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

###############################################################################
import re

# inp = test_input
inp = open('data/input05').read()


def part1(inp):
    sections = inp.split('\n\n')
    seeds = list(map(int, re.findall('\d+', sections[0])))
    for section in sections[1:]:
        numbers_part = section.split('\n')[1:]

        new_seeds = []
        for seed in seeds:
            new_seed = seed
            for numbers in numbers_part:
                numbers = list(map(int, re.findall('\d+', numbers)))
                dest, source, rng = numbers
                if source <= seed < source + rng:
                    i = seed - source
                    new_seed = dest + i
            new_seeds.append(new_seed)

        seeds = new_seeds

    print(f"part1: {min(seeds)}")


part1(inp)

###############################################################################
from functools import lru_cache
from tqdm import tqdm

inp = test_input
# inp = open('data/input05').read()

sections = inp.split('\n\n')
parsed_sections = []
for i in range(1, len(sections)):
    parsed_section = [list(map(int, re.findall('\d+', section))) for section in sections[i].split('\n')[1:]]
    parsed_sections.append(parsed_section)

def is_in_range(tup, source_start, source_stop):
    """Returns bool, list of tuples to shift, list of tuples that don’t need to be shifted."""
    if tup[0] < source_start:
        return False, None, None
    elif (tup[0] < source_start) and (tup[1] < source_stop):
        return True, [(source_start, tup[1])], [(tup[0], source_start)]
    # tup is fully within boundaries of source
    elif (tup[0] >= source_start) and (tup[1] < source_stop):
        return True, [(tup[0], tup[1])], None
    elif (tup[0] >= source_start) and (tup[1] > source_stop):
        return True, [(tup[0], source_stop)], [(source_stop, tup[1])]
    elif (tup[0] <= source_start) and (tup[1] > source_stop):
        return True, [(source_start, source_stop)], [(tup[0], source_start), (source_stop, tup[1])]
    else:
        return False, None, None



def input_to_output(seed_tuple): # (79, 79 + 14) = (start, stop)
    input_seeds = [seed_tuple]
    for section in parsed_sections:
        while len(input_seeds) > 0:
            current_tup = input_seeds.pop()
            output_seeds = []
            has_been_added = False
            for dest, source, rng in section:
                source_start, source_stop = source, source + rng
                in_range, tup_to_shift, tup_intact = is_in_range(current_tup, source_start, source_stop)
                if in_range:
                    for t in tup_to_shift:
                        offset = dest - source_start
                        t = (t[0] + offset, t[1] + offset)
                        output_seeds.append(t)
                    if tup_intact:
                        input_seeds.extend(tup_intact)
                    has_been_added = True
                    break
            if not has_been_added:
                output_seeds.append(current_tup)
        input_seeds = output_seeds
    return output_seeds

seeds = list(map(int, re.findall('\d+', sections[0])))
seed_lists = [(start, start + rng_len) for start, rng_len in zip(seeds[::2], seeds[1::2])]
input_to_output(seed_lists[0])

###############################################################################

def part2(inp):
    seeds = list(map(int, re.findall('\d+', sections[0])))
    seed_lists = [(start, start + rng_len) for start, rng_len in zip(seeds[::2], seeds[1::2])]

    minima = []
    for start, stop in tqdm(seed_lists):
        outputs = [input_to_output(seed) for seed in tqdm(range(start, stop))]
        minima.append(min(outputs))

    print(f"part2: {min(minima)}")


# 63979762 too high
part2(inp)

###############################################################################
sections = inp.split('\n\n')
seeds = list(map(int, re.findall('\d+', sections[0])))
seed_lists = [(start, start + rng_len) for start, rng_len in zip(seeds[::2], seeds[1::2])]

###############################################################################

