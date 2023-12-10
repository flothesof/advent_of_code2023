test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# inp = test_input
inp = open('data/input09').read()
sequences = [list(map(int, line.split(' '))) for line in inp.split('\n')]

def diff(s):
    return [n - p for n, p in zip(s[1:], s[:-1])]

s = sequences[0]
while sum(s) != 0:
    s = diff(s)
    break
###############################################################################
def extrapolate(s):
    if sum([abs(i) for i in s]) == 0:
        return 0
    else:
        return s[-1] + extrapolate(diff(s))

part1 = sum(extrapolate(s) for s in sequences)

# 2038472403 too high
part1
###############################################################################

def backwards(s):
    if sum([abs(i) for i in s]) == 0:
        return 0
    else:
        return s[0] - backwards(diff(s))

part2 = sum(backwards(s) for s in sequences)

part2
###############################################################################

