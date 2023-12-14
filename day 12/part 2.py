import re
import time
t = time.perf_counter()

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(input_line, do_unfold=False):
    left, right = input_line.split(' ')
    if do_unfold:
        left, right = unfold(left, right)
    left = list(left)
    for i in range(len(left)):
        if left[i] == '.':
            left[i] = 0
        elif left[i] == '#':
            left[i] = 1
        else:
            left[i] = -1

    return left, [int(i) for i in re.findall(r'\d+', right)]


def is_invalid(input_row, contiguous_blocks, block_positions):
    for block, (current_block_position, next_block_position) in enumerate(zip(block_positions, block_positions[1:])):
        if next_block_position <= current_block_position + contiguous_blocks[block]:
            return True

    num_blocks = len(block_positions)
    actual_row = [0 for _ in range(block_positions[-1] + contiguous_blocks[num_blocks - 1])]
    if len(contiguous_blocks) == num_blocks:
        actual_row = [0 for _ in input_row]

    for block_size, position in zip(contiguous_blocks, block_positions):
        for i in range(block_size):
            if position + i >= len(actual_row):
                return True
            actual_row[position + i] = 1

    for expected_value, actual_value in zip(input_row, actual_row):
        if expected_value == -1:
            continue

        if expected_value != actual_value:
            return True

    return False


def get_number_of_solutions(input_row, contiguous_blocks):
    possible_block_positions = [list(range(len(input_row))) for _ in contiguous_blocks]

    total_solutions = 0

    block_position_indices = [-1 for _ in possible_block_positions]
    block_index = 0
    calculated_values = {}
    values_being_counted = {}
    stepped_forward = False
    stepped_backward = False
    frontier = 0
    while block_index > -1:
        if stepped_forward:
            stepped_forward = False
            frontier = block_position_indices[block_index - 1]
            if (frontier, block_index) in calculated_values:
                total_solutions += calculated_values[(frontier, block_index)]
                for state in values_being_counted:
                    values_being_counted[state] += calculated_values[(frontier, block_index)]
                stepped_backward = True
                block_index -= 1
                continue

            values_being_counted[(frontier, block_index)] = 0

            if block_index >= len(block_position_indices):
                for state in values_being_counted:
                    values_being_counted[state] += 1
                total_solutions += 1
                stepped_backward = True
                block_index -= 1
                continue

        if stepped_backward:
            stepped_backward = False
            if (frontier, block_index + 1) not in calculated_values:
                calculated_values[(frontier, block_index + 1)] = values_being_counted.pop((frontier, block_index + 1))

            frontier = block_position_indices[block_index - 1]

        block_position_indices[block_index] += 1

        if block_position_indices[block_index] >= len(possible_block_positions[block_index]):
            block_position_indices[block_index] = -1

            stepped_backward = True
            block_index -= 1
            continue

        block_positions = [possible_block_positions[i][j] for i, j in enumerate(block_position_indices) if j != -1]
        if is_invalid(input_row, contiguous_blocks, block_positions):
            continue

        stepped_forward = True
        block_index += 1

    return total_solutions


def print_row(input_row):
    for i in input_row:
        if i == -1 or i == {0, 1}:
            print('?', end='')
        elif i == 0 or i == {0}:
            print('.', end='')
        else:
            print('#', end='')
    print('')


def unfold(input_row, contiguous_blocks):
    return '?'.join([input_row for _ in range(5)]), ','.join([contiguous_blocks for _ in range(5)])


total = 0
for line_index, line in enumerate(puzzle_input):
    row, blocks = parse_line(line, do_unfold=True)
    print(f'problem {line_index}:')
    print_row(row)
    print(blocks)
    n = get_number_of_solutions(row, blocks)
    total += n
    print(n)
    print('')
print(total)
print(time.perf_counter() - t)
