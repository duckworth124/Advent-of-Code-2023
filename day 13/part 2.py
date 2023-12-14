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


def get_horizontal_split(input_pattern):
    output = set()
    for split_position in range(1, len(input_pattern)):
        if test_horizontal_split(input_pattern, split_position):
            output.add(split_position)
    return output


def get_vertical_split(input_pattern):
    output = set()
    for split_position in range(1, len(input_pattern[0])):
        if test_vertical_split(input_pattern, split_position):
            output.add(split_position)
    return output


def fix_smudge(input_pattern, x, y):
    input_pattern = [[i for i in row] for row in input_pattern]
    if input_pattern[y][x] == '.':
        input_pattern[y][x] = '#'
    else:
        input_pattern[y][x] = '.'
    return [''.join(i) for i in input_pattern]


def find_smudge(input_pattern):
    old_vertical = get_vertical_split(input_pattern)
    old_horizontal = get_horizontal_split(input_pattern)
    for y_position, row in enumerate(input_pattern):
        for x_position, value in enumerate(row):
            new_pattern = fix_smudge(input_pattern, x_position, y_position)
            new_vertical, new_horizontal = get_vertical_split(new_pattern), get_horizontal_split(new_pattern)
            if not new_vertical.difference(old_vertical).issubset({0}):
                return new_vertical.difference(old_vertical), set()
            if not new_horizontal.difference(old_horizontal).issubset({0}):
                return set(), new_horizontal.difference(old_horizontal)

    return 0, 0


summary = 0

for pattern in puzzle_input:
    print_pattern(pattern)

    vertical, horizontal = find_smudge(pattern)
    if vertical == set and horizontal == set():
        raise Exception
    summary += sum(vertical)
    summary += 100 * sum(horizontal)
    print(vertical)
    print(horizontal)
    print(summary)
    print('')

print(summary)
