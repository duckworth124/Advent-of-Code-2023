with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n\n')
puzzle_input = [i.split('\n') for i in puzzle_input]


def print_pattern(input_pattern):
    for row in input_pattern:
        print(row)


def transpose(input_pattern):
    output = [[] for _ in input_pattern[0]]
    for row in input_pattern:
        for index, value in enumerate(row):
            output[index].append(value)
    output = [''.join(i) for i in output]
    return output


def test_vertical_split(input_pattern, input_split_position):
    for y_position, row in enumerate(input_pattern):
        for x_position, value in enumerate(row[:input_split_position]):
            reflected_x_position = input_split_position + (input_split_position - x_position) - 1
            if reflected_x_position not in range(len(row)):
                continue
            if value != row[reflected_x_position]:
                return False
    return True


def test_horizontal_split(input_pattern, input_split_position):
    return test_vertical_split(transpose(input_pattern), input_split_position)


def get_horizontal_splits(input_pattern):
    output = []
    for split_position in range(1, len(input_pattern)):
        if test_horizontal_split(input_pattern, split_position):
            output.append(split_position)
    return output


def get_vertical_splits(input_pattern):
    output = []
    for split_position in range(1, len(input_pattern[0])):
        if test_vertical_split(input_pattern, split_position):
            output.append(split_position)
    return output


summary = 0

for pattern in puzzle_input:
    print_pattern(pattern)
    vertical, horizontal = get_vertical_splits(pattern), get_horizontal_splits(pattern)
    if vertical == [] and horizontal == []:
        raise Exception
    summary += sum(vertical)
    summary += 100 * sum(horizontal)
    print(vertical)
    print(horizontal)
    print('')

print(summary)
