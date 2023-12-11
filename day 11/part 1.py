import itertools

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def get_empty_lines():
    rows = []
    columns = []
    for row_index, row in enumerate(puzzle_input):
        if '#' not in row:
            rows.append(row_index)

    for column_index in range(len(puzzle_input[0])):
        column = [row[column_index] for row in puzzle_input]
        if '#' not in column:
            columns.append(column_index)

    return rows, columns


def get_galaxies():
    positions = []
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            if puzzle_input[y][x] == '#':
                positions.append((x, y))
    return positions


empty_rows, empty_columns = get_empty_lines()
galaxies = get_galaxies()


def get_distance(input_galaxy1, input_galaxy2):
    x1, y1 = input_galaxy1
    x2, y2 = input_galaxy2
    total_distance = abs(x1 - x2) + abs(y1 - y2)
    for row in empty_rows:
        if y1 < row < y2 or y2 < row < y1:
            total_distance += 1

    for column in empty_columns:
        if x1 < column < x2 or x2 < column < x1:
            total_distance += 1

    return total_distance


total = 0
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
    total += get_distance(galaxy1, galaxy2)
print(total)
