import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    number_positions = {}
    line = re.finditer(r'\d+', line)
    for number in line:
        number_positions[(number.start(), number.end())] = int(number.group())

    return number_positions


def is_star_adjacent(position, line_index, star_i, star_j):
    start_pos, end_pos = position
    return line_index - 1 <= star_i <= line_index + 1 and start_pos - 1 <= star_j < end_pos + 1


def is_gear(line_index, pos_in_line):
    global puzzle_input_parsed
    adjacent_number_count = 0
    adjacent_numbers = []
    for adjacent_line_index in range(min(line_index - 1, 0), max(line_index + 2, len(puzzle_input))):
        line = puzzle_input_parsed[adjacent_line_index]
        for position in line:
            if is_star_adjacent(position, adjacent_line_index, line_index, pos_in_line):
                adjacent_number_count += 1
                adjacent_numbers.append(line[position])

    return adjacent_number_count == 2, adjacent_numbers


puzzle_input_parsed = [parse_line(line) for line in puzzle_input]
total = 0
for line_index, line in enumerate(puzzle_input):
    for pos_in_line in range(len(line)):
        if line[pos_in_line] == '*':
            is_this_a_gear, numbers = is_gear(line_index, pos_in_line)
            if is_this_a_gear:
                ratio = numbers[0] * numbers[1]
                total += ratio


print(total)
