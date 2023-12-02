import re

# part 2
def power(counts):
    p = 1
    for val in counts.values():
        p = p*val
    return p


lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = open('data/input02').read()

game_id_count = 0
sum_powers = 0
for line in lines.split('\n'):
    max_count = {'red': 0, 'green': 0, 'blue': 0}
    game_id = int(line.split(':')[0][5:])
    for game in line.split(':')[1].split(';'):
        for color in max_count:
            m = re.findall(r'(\d+) ' + color, game)
            if m:
                max_count[color] = max(max_count[color], int(m[0]))
    print(max_count)
    if (max_count['red'] <= 12) and (max_count['green'] <= 13) and (max_count['blue'] <= 14):
        game_id_count += game_id
    sum_powers += power(max_count)

game_id_count, sum_powers
###############################################################################


