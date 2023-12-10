import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    game_id = int(re.search(r'\d+', line).group(0))
    rgb = {'red': 0, 'blue': 0, 'green': 0}
    line = line.split(':')[1]
    line = line.split(';')
    for cubes in line:
        for colour in rgb:
            cubes_of_this_colour = re.search(r'(\d+) ' + colour, cubes)
            if cubes_of_this_colour is None:
                continue

            count = int(cubes_of_this_colour.group(1))
            rgb[colour] = max(rgb[colour], count)

    return game_id, rgb


total = 0
for line in puzzle_input:
    game_id, rgb = parse_line(line)
    power = 1
    for count in rgb.values():
        power *= count
    total += power
print(total)
