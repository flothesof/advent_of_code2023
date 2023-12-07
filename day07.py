from functools import cmp_to_key
from collections import Counter

mapping = dict(zip('AKQJT98765432', range(13, 0, -1)))


def cmp_hands(hand1, hand2):
    type_hand1 = hand_type(hand1)
    type_hand2 = hand_type(hand2)
    if type_hand1 != type_hand2:
        return type_hand1 - type_hand2
    else:
        for first, second in zip(hand1, hand2):
            if first != second:
                return mapping[first] - mapping[second]
        return 0


def hand_type(hand):
    c = Counter(hand)
    vals = sorted(list(c.values()), reverse=True)
    if len(c) == 1:
        return 7
    elif len(c) == 2:
        if vals[0] == 4:
            return 6
        elif vals[0] == 3 and vals[1] == 2:
            return 5
    elif len(c) == 3:
        if vals[0] == 3:
            return 4
        elif vals[0] == 2 and vals[1] == 2:
            return 3
    elif vals[0] == 2:
        return 2
    else:
        return 1


assert hand_type('TTTTT') == 7
assert hand_type('AA8AA') == 6
assert hand_type('23332') == 5
assert hand_type('TTT98') == 4
assert hand_type('23432') == 3
assert hand_type('A23A4') == 2
assert hand_type('23456') == 1

###############################################################################
test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# inp = test_input
inp = open('data\input07').read()

hands = [line.split(' ')[0] for line in inp.split('\n')]
bids = list(map(int, [line.split(' ')[1] for line in inp.split('\n')]))

sorted_hands = sorted(hands, key=cmp_to_key(cmp_hands))

part1 = 0
for hand, bid in zip(hands, bids):
    print(hand, bid, sorted_hands.index(hand) + 1)
    part1 += bid * (sorted_hands.index(hand) + 1)

print('part1: ', part1)
###############################################################################
# part 2
mapping_part2 = dict(zip('AKQJT98765432J', range(13, -1, -1)))


def cmp_hands_part2(hand1, hand2):
    type_hand1 = hand_type_part2(hand1)
    type_hand2 = hand_type_part2(hand2)
    if type_hand1 != type_hand2:
        return type_hand1 - type_hand2
    else:
        for first, second in zip(hand1, hand2):
            if first != second:
                return mapping_part2[first] - mapping_part2[second]
        return 0


def hand_type_part2(hand):
    n_jokers = hand.count('J')
    c = Counter(hand.replace('J', ''))
    vals = sorted(list(c.values()), reverse=True)
    if len(vals) > 0:
        vals[0] += n_jokers
    else:
        # special case only jokers
        return 7
    if len(c) == 1:
        return 7
    elif len(c) == 2:
        if vals[0] == 4:
            return 6
        elif vals[0] == 3 and vals[1] == 2:
            return 5
    elif len(c) == 3:
        if vals[0] == 3:
            return 4
        elif vals[0] == 2 and vals[1] == 2:
            return 3
    elif vals[0] == 2:
        return 2
    else:
        return 1


assert hand_type_part2('TTTTT') == 7
assert hand_type_part2('AA8AA') == 6
assert hand_type_part2('23332') == 5
assert hand_type_part2('TTT98') == 4
assert hand_type_part2('23432') == 3
assert hand_type_part2('A23A4') == 2
assert hand_type_part2('23456') == 1
assert hand_type_part2('T55J5') == 6
assert hand_type_part2('KTJJT') == 6
assert hand_type_part2('QQQJA') == 6
assert hand_type_part2('JJJJJ') == 7
assert hand_type_part2('QJJQ2') == 6
assert cmp_hands_part2('JKKK2', 'QQQQ2') < 0

###############################################################################

test_input2 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# inp = test_input2
inp = open('data\input07').read()

hands = [line.split(' ')[0] for line in inp.split('\n')]
bids = list(map(int, [line.split(' ')[1] for line in inp.split('\n')]))

sorted_hands = sorted(hands, key=cmp_to_key(cmp_hands_part2))

part2 = 0
for hand, bid in zip(hands, bids):
    print(hand, bid, sorted_hands.index(hand) + 1)
    part2 += bid * (sorted_hands.index(hand) + 1)

# 250545770 too low
# 250661817 too high
print('part2: ', part2)

###############################################################################
