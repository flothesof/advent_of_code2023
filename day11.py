def rotate(lines):
    I = len(lines)
    J = len(lines[0])
    out = [str() for i in range(J)]
    for i in range(I):
        for j in range(J):
            out[j] += lines[i][j]
    return out


rotate(["abc", "def"])

###############################################################################
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
inp = open('data\input11').read()

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
