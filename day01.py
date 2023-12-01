from functools import partial


def first_digit(line, reverse=False):
    if reverse:
        line = "".join(reversed(line))
    for char in line:
        if char in '0123456789':
            return char


last_digit = partial(first_digit, reverse=True)

# test_line = 'auirsetur1ruiters2'
test_line = 'eight691seven8cxdbveightzv'
first_digit(test_line), last_digit(test_line)

###############################################################################
test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

# lines = test_input.split("\n")
lines = open('data/input01').readlines()

sum = 0
for line in lines:
    line = line.strip()
    chars = first_digit(line) + last_digit(line)
    print(line, chars)
    sum += int(chars)

print(f"sum: {sum}")

###############################################################################
# Part 2:
replacement_dict = {'one': '1',
                    'two': '2',
                    'three': '3',
                    'four': '4',
                    'five': '5',
                    'six': '6',
                    'seven': '7',
                    'eight': '8',
                    'nine': '9',
                    'zero': '0'}


def replace_numbers(line):
    for number in replacement_dict:
        line = line.replace(number, replacement_dict[number])
    return line


line = 'eight691seven8cxdbveightzv'
replace_numbers(line)


###############################################################################
def first_digit_part2(line):
    for ind, char in enumerate(line):
        if char in '0123456789':
            return char
        else:
            for number in replacement_dict:
                if line[ind:].startswith(number):
                    return replacement_dict[number]


def last_digit_part2(line):
    line = "".join(reversed(line))
    for ind, char in enumerate(line):
        if char in '0123456789':
            return char
        else:
            for number in replacement_dict:
                if line[ind:].startswith(number[::-1]):
                    return replacement_dict[number]


test_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

# lines = test_input2.split("\n")
lines = open('data/input01').readlines()

sum = 0
for line in lines:
    line = line.strip()
    chars = first_digit_part2(line) + last_digit_part2(line)
    print(line, chars)
    sum += int(chars)

print(f"part 2: {sum}")

###############################################################################
