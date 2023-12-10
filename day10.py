test_input1 = """.....
.S-7.
.|.|.
.L-J.
.....""", 'F'

test_input2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""", 'F'

test_input3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""", 'F'

test_input4 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........""", 'F'

test_input5 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""", "F"


def make_tiles(inp):
    tiles = {}
    I, J = len(inp.split('\n')), len(inp.split('\n')[0])
    for i, line in enumerate(inp.split('\n')):
        for j, val in enumerate(line):
            tiles[(i, j)] = val
            if val == 'S':
                start = (i, j)
    return tiles, start, I, J


connections = {'F': ('E', 'S'),
               'L': ('E', 'N'),
               'J': ('W', 'N'),
               '7': ('W', 'S'),
               '|': ('N', 'S'),
               '-': ('E', 'W')}

steps = {'E': (0, 1),
         'W': (0, -1),
         'N': (-1, 0),
         'S': (1, 0)}

inp, start_value = test_input5
# inp, start_value = open('data/input10').read(), 'J'

# make a map
tiles, start, I, J = make_tiles(inp)
tiles[start] = start_value

# explore tiles
main_loop = {start: 0}
active_tiles = [start]
while len(active_tiles):
    active_tiles = sorted(active_tiles, key=lambda k: main_loop[k])
    coord = active_tiles.pop(0)
    conns = connections[tiles[coord]]
    for direction in conns:
        step = steps[direction]
        new_coord = (coord[0] + step[0], coord[1] + step[1])
        if new_coord not in main_loop:
            active_tiles.append(new_coord)
            main_loop[new_coord] = main_loop[coord] + 1

print("part 1:", max(main_loop.values()))

###############################################################################

count_inside_i = set()
for i, line in enumerate(inp.split('\n')):
    outside = 0
    for j, val in enumerate(line):
        if val == 'S':
            val = start_value

        if val == '.':
            if outside % 2 == 0:
                continue
            else:
                count_inside_i.add((i, j))
        elif (i, j) in main_loop:
            if val == '|':
                outside += 1
            elif val in 'LF':
                outside += 1
            elif val in 'J7':
                outside -= 1

count_inside_i

count_inside_j = set()
for j in range(J):
    outside = 0
    for i in range(I):
        val = inp.split('\n')[i][j]
        if val == 'S':
            val = start_value

        if val == '.':
            if outside % 2 == 0:
                continue
            else:
                count_inside_j.add((i, j))
        elif (i, j) in main_loop:
            if val == '-':
                outside += 1
            elif val in 'F7':
                outside += 1
            elif val in 'JL':
                outside -= 1

count_inside_j

print("part2:", len(count_inside_i.intersection(count_inside_j)))

###############################################################################
len(count_inside_i), len(count_inside_j)
###############################################################################

