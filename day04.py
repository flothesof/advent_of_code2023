import re
from collections import defaultdict

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# inp = test_input
inp = open('data/input04').read()

points = 0
for line in inp.split('\n'):
    winning_numbers, my_numbers = line.strip().split(' | ')
    winning_numbers = re.split('\s+', winning_numbers.split(': ')[1].strip())
    my_numbers = re.split('\s+', my_numbers)
    intersection = set(my_numbers).intersection(set(winning_numbers))
    assert len(intersection) <= len(winning_numbers)
    print(line, winning_numbers, my_numbers, intersection)
    if len(intersection) > 0:
        worth = 2 ** (len(intersection) - 1)
        points += worth

# 26529 too high
# 25340 too high
points

###############################################################################
# part 2:

# inp = test_input
inp = open('data/input04').read()

points = 0
my_cards = defaultdict(lambda: 1)
for line in inp.split('\n'):
    winning_numbers, my_numbers = line.strip().split(' | ')
    card_number = int(re.match('Card\s+(\d+)', winning_numbers).groups()[0])
    my_cards[card_number] # init card number to be 1 with the defaultdict constructor
    winning_numbers = re.split('\s+', winning_numbers.split(': ')[1].strip())
    my_numbers = re.split('\s+', my_numbers)
    intersection = set(my_numbers).intersection(set(winning_numbers))
    assert len(intersection) <= len(winning_numbers)
    if len(intersection) > 0:
        for i in range(card_number + 1, card_number + len(intersection) + 1):
            my_cards[i] += my_cards[card_number]

print(f"part 2: {sum(my_cards.values())}")

###############################################################################
