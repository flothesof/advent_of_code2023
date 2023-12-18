def rotate(lines):
    I = len(lines)
    J = len(lines[0])
    out = [str() for i in range(J)]
    for i in range(I):
        for j in range(J):
            out[j] += lines[i][j]
    return out


# rotate(["abc", "def"])

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

# inp = test_input
inp = open('data/input11').read()

lines = inp.split('\n')

# add missing lines
processed_lines = []
for line in lines:
    if line.find('#') < 0:
        processed_lines.append(line)
        processed_lines.append(line)
    else:
        processed_lines.append(line)

# add missing columns
N = len(line)
lines = rotate(processed_lines)

processed_lines = []
for line in lines:
    if line.find('#') < 0:
        processed_lines.append(line)
        processed_lines.append(line)
    else:
        processed_lines.append(line)

processed_lines = rotate(processed_lines)

# indexing galaxies
galaxies = set()
for i, line in enumerate(processed_lines):
    for j, val in enumerate(line):
        if val == '#':
            galaxies.add((i, j))

# computing distances
dists = {}
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies):
        if i != j:
            a, b = g1
            c, d = g2
            if (g2 + g1) not in dists:
                dists[(g1 + g2)] = abs(a - c) + abs(b - d)

print('part1: ', sum(dists.values()))

###############################################################################
# part 2:
# inp = test_input
inp = open('data/input11').read()

lines = inp.split('\n')

# add missing lines
missing_lines = []
for i, line in enumerate(lines):
    if line.find('#') < 0:
        missing_lines.append(i)


def cols(lines):
    N = len(lines)
    M = len(lines[0])
    for j in range(M):
        l = ""
        for i in range(N):
            l += lines[i][j]
        yield l


missing_cols = []
for j, col in enumerate(cols(lines)):
    if col.find('#') < 0:
        missing_cols.append(j)


def remap(i, j, multiplier=1000000):
    return (i + sum(multiplier - 1 for ii in missing_lines if ii < i),
            j + sum(multiplier - 1 for jj in missing_cols if jj < j))


# indexing galaxies
galaxies = set()
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == '#':
            galaxies.add(remap(i, j))

# computing distances
dists = {}
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies):
        if i != j:
            a, b = g1
            c, d = g2
            if (g2 + g1) not in dists:
                dists[(g1 + g2)] = abs(a - c) + abs(b - d)

print('part2: ', sum(dists.values()))

###############################################################################
