import re

from matplotlib import pyplot as plt
from tqdm import tqdm

test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

# inp = test_input
inp = open('data/input14').read()

grid = {}
for r, line in enumerate(inp.split('\n')):
    for c, item in enumerate(line):
        grid[(r, c)] = item

###############################################################################
# let’s push stuff north
n_cols = len(inp.split('\n')[0])
n_rows = len(inp.split('\n'))


def get_col(col):
    c = ''
    for r in range(n_rows):
        c += grid[(r, col)]
    return c


new_grid = {}
for c in range(n_cols):
    col = get_col(c)
    splits = re.split('(#+)', col)
    reordered = ''
    for seq in splits:
        if '#' in seq:
            reordered += seq
        else:
            cnt = sum(1 for cc in seq if cc == 'O')
            reordered += 'O' * cnt
            reordered += '.' * (len(seq) - cnt)
    for r in range(n_rows):
        new_grid[(r, c)] = reordered[r]


###############################################################################
def compute_weight(new_grid):
    part1 = 0

    for r in range(n_rows):
        weight = n_rows - r
        cnt = sum(1 for c in range(n_cols) if new_grid[(r, c)] == 'O')
        part1 += weight * cnt
    return part1


part1 = compute_weight(new_grid)


###############################################################################

def get_col_with_dir(row_or_col, grid, dir='north'):
    out_row_or_col = ''
    if dir == 'north':
        for r in range(n_rows):
            out_row_or_col += grid[(r, row_or_col)]
    elif dir == 'south':
        for r in range(n_rows - 1, -1, -1):
            out_row_or_col += grid[(r, row_or_col)]
    elif dir == 'east':
        for c in range(n_cols):
            out_row_or_col += grid[(row_or_col, c)]
    elif dir == 'west':
        for c in range(n_cols - 1, -1, -1):
            out_row_or_col += grid[(row_or_col, c)]
    return out_row_or_col


def reorder(row_or_col):
    splits = re.split('(#+)', row_or_col)
    reordered = ''
    for seq in splits:
        if '#' in seq:
            reordered += seq
        else:
            cnt = sum(1 for cc in seq if cc == 'O')
            reordered += 'O' * cnt
            reordered += '.' * (len(seq) - cnt)
    return reordered


def print_grid(grid):
    for r in range(n_rows):
        l = get_col_with_dir(r, grid, 'east')
        print(l)


# print_grid(grid)
# print('-------')
# print_grid(new_grid)
# print('-------')


###############################################################################
def rotate(grid, dir):
    reverse = False
    new_grid = {}
    if dir in ['north', 'south']:
        if dir == 'south':
            reverse = True
        for c in range(n_cols):
            reordered = reorder(get_col_with_dir(c, grid, dir=dir))
            if reverse:
                reordered = list(reversed(reordered))
            for r in range(n_rows):
                new_grid[(r, c)] = reordered[r]
    elif dir in ['east', 'west']:
        if dir == 'west':
            reverse = True
        for r in range(n_rows):
            reordered = reorder(get_col_with_dir(r, grid, dir=dir))
            if reverse:
                reordered = list(reversed(reordered))
            for c in range(n_cols):
                new_grid[(r, c)] = reordered[c]
    assert len(new_grid) == n_rows * n_cols
    return new_grid


def cycle(grid):
    # print_grid(grid)
    # print('---after north---')
    grid = rotate(grid, 'north')
    # print_grid(grid)
    # print('-----after west----')
    grid = rotate(grid, 'east')
    # print_grid(grid)
    # print('---after south----')
    grid = rotate(grid, 'south')
    # print_grid(grid)
    # print('--after east---')
    grid = rotate(grid, 'west')
    # print_grid(grid)
    return grid


# print_grid(grid)
# print('--after 1--')
# grid = cycle(grid)
# print_grid(grid)
# print('-- after 2---')
# grid = cycle(grid)
# print_grid(grid)
# print('---after 3--')
# grid = cycle(grid)
# print_grid(grid)

def grid_hash(grid):
    return "".join(grid.values())

burnin = 200
vals = []
mapping = {}
for i in tqdm(range(400)):
    grid = cycle(grid)
    val = compute_weight(grid)
    vals.append(val)

    if i >= burnin:
        if not (val, grid_hash(grid))  in mapping:
            mapping[(val, grid_hash(grid))] = i
        else:
            break

rev_mapping = {v:k for k, v in mapping.items()}
period = i - burnin
print('period of series is:', period)
# 102048 too low
plt.plot(vals)
plt.show()
###############################################################################
ind = (1000000000 - burnin - 1) % period
print('value at i=1000000000', rev_mapping[ind + burnin][0])

###############################################################################

