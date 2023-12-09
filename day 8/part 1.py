import itertools
import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    return re.findall(r'\w+', line)


directions = puzzle_input[0]
paths = {}
for line in puzzle_input[2:]:
    pos, left, right = parse_line(line)
    paths[pos] = {'L': left, 'R': right}

number_of_steps = 0
current_pos = 'AAA'
for direction in itertools.cycle(directions):
    current_pos = paths[current_pos][direction]
    number_of_steps += 1
    if current_pos == 'ZZZ':
        break
print(number_of_steps)
