import re

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def prepare_input(inp):
    lines = inp.split('\n')
    N = len(lines[0])
    lines = ['.' + line.strip() + '.' for line in lines]
    lines.insert(0, '.' * (N + 2))
    lines.insert(len(lines), '.' * (N + 2))
    return lines


prepare_input(test_input)

###############################################################################
inp = open('data/input03').read()
# inp = test_input

prepared_input = prepare_input(inp)
part_number_sum = 0
all_numbers = []
for line_ind, line in enumerate(prepared_input):
    for match in re.finditer(r'\d+', line.strip()):
        number = match.group()
        all_numbers.append(number)
        neigbors = []
        for index in range(match.start(), match.end()):
            if index == match.start():
                neigbors.extend([prepared_input[line_ind - 1][index - 1],
                                 prepared_input[line_ind][index - 1],
                                 prepared_input[line_ind + 1][index - 1]])
            if index == match.end() - 1:
                neigbors.extend([prepared_input[line_ind - 1][index + 1],
                                 prepared_input[line_ind][index + 1],
                                 prepared_input[line_ind + 1][index + 1]])

            neigbors.extend([prepared_input[line_ind - 1][index],
                             prepared_input[line_ind + 1][index]])
            index += 1
        diff_set = set(neigbors).difference(set('.'))
        print(f"line: {line_ind: 3}, number: {number:4}, neigbors: {neigbors}, diff_set: {diff_set}")
        if len(diff_set) > 0:
            # print(f"line: {line_ind}, number: {int(number)} is part number, symbol: {diff_set}")
            part_number_sum += int(number)

# 548941 too high,
# 538361 too high,
# 537804 not right,
# 536129 not right,
# 530291 not right,
# 531966 not right

print(f"part 1: sum of part numbers {part_number_sum}")
with open('numbers.txt', 'w') as f:
    f.writelines("\n".join(all_numbers))

###############################################################################
# part 2: gears

inp = open('data/input03').read()
# inp = test_input

def val_and_coords(array, line, row):
    return array[line][row], (line, row)

prepared_input = prepare_input(inp)
part_number_sum = 0
all_numbers = []
star_connections = {}
for line_ind, line in enumerate(prepared_input):
    for match in re.finditer(r'\d+', line.strip()):
        number = match.group()
        all_numbers.append(number)
        neigbors = []
        for index in range(match.start(), match.end()):
            if index == match.start():
                neigbors.extend([val_and_coords(prepared_input, line_ind - 1, index - 1),
                                 val_and_coords(prepared_input, line_ind, index - 1),
                                 val_and_coords(prepared_input, line_ind + 1, index - 1)])

            if index == match.end() - 1:
                neigbors.extend([val_and_coords(prepared_input, line_ind - 1, index + 1),
                                 val_and_coords(prepared_input, line_ind, index + 1),
                                 val_and_coords(prepared_input, line_ind + 1, index + 1)])

            neigbors.extend([val_and_coords(prepared_input,line_ind - 1,index),
                             val_and_coords(prepared_input, line_ind + 1, index)])
            index += 1
        diff_set = set([n[0] for n in neigbors]).difference(set('.'))
        if len(diff_set) > 0:
            part_number_sum += int(number)
            # print(f"line: {line_ind}, number: {int(number)} is part number, symbol: {diff_set}")
            if "*" in diff_set:
                print(f"line: {line_ind: 3}, number: {number:4}, neigbors: {neigbors}, diff_set: {diff_set}")
                star_neighbors = [n for n in neigbors if n[0] == '*']
                assert len(star_neighbors) == 1
                star_coords = star_neighbors[0][1]
                if star_coords in star_connections:
                    star_connections[star_coords].append(int(number))
                else:
                    star_connections[star_coords] = [int(number)]

prod = lambda l: l[0] * l[1]
print(sum([prod(star_connections[sc]) for sc in star_connections if len(star_connections[sc]) == 2]))
###############################################################################
