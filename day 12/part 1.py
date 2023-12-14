import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(input_line):
    left, right = input_line.split(' ')
    left = list(left)
    for i in range(len(left)):
        if left[i] == '.':
            left[i] = 0
        elif left[i] == '#':
            left[i] = 1
        else:
            left[i] = -1

    return left, [int(i) for i in re.findall(r'\d+', right)]


def get_contiguous_blocks(input_row):
    contiguous_blocks = []
    currently_in_block = False
    for i in input_row:
        if i == 1:
            if currently_in_block:
                contiguous_blocks[-1] += 1
                continue
            contiguous_blocks.append(1)
            currently_in_block = True
            continue

        currently_in_block = False
    return contiguous_blocks


def is_invalid(input_row, contiguous_blocks, last_point_changed, is_complete=False):
    actual_contiguous_blocks = get_contiguous_blocks(input_row[:last_point_changed + 1])
    if is_complete:
        return contiguous_blocks != actual_contiguous_blocks
    blocks_to_compare = zip(actual_contiguous_blocks[:-1], contiguous_blocks)
    for block1, block2 in blocks_to_compare:
        if block1 != block2:
            return True
    return False


def get_number_of_solutions(input_row, contiguous_blocks):
    unknown_points = [index for index, element in enumerate(input_row) if element == -1]
    current_unknown_point = 0
    total_solutions = 0
    while current_unknown_point > -1:
        if current_unknown_point >= len(unknown_points):
            if not is_invalid(input_row, contiguous_blocks, len(input_row) - 1, is_complete=True):
                total_solutions += 1
            current_unknown_point -= 1
            continue

        input_row[unknown_points[current_unknown_point]] += 1
        if input_row[unknown_points[current_unknown_point]] >= 2:
            input_row[unknown_points[current_unknown_point]] = -1
            current_unknown_point -= 1
            continue

        if is_invalid(input_row, contiguous_blocks, unknown_points[current_unknown_point]):
            continue

        current_unknown_point += 1

    return total_solutions


def print_row(input_row):
    for i in input_row:
        if i == -1:
            print('?', end='')
        elif i == 0:
            print('.', end='')
        else:
            print('#', end='')
    print('')


total = 0
for line in puzzle_input:
    row, blocks = parse_line(line)
    total += get_number_of_solutions(row, blocks)
print(total)
