import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    number_positions = {}
    line = re.finditer(r'\d+', line)
    for number in line:
        number_positions[(number.start(), number.end())] = int(number.group())

    return number_positions


def is_symbol_adjacent(position, line_index):
    start_pos, end_pos = position
    for i in range(max(line_index - 1, 0), min(line_index + 2, len(puzzle_input))):
        for j in range(max(start_pos - 1, 0), min(end_pos + 1, len(puzzle_input[0]))):
            if not puzzle_input[i][j].isdigit() and puzzle_input[i][j] != '.':
                return True
    return False


total = 0
for line_index, line in enumerate(puzzle_input):
    number_positions = parse_line(line)
    for position, number in number_positions.items():
        if is_symbol_adjacent(position, line_index):
            total += number

print(total)
