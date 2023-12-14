with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(input_line):
    output = []
    for i in input_line:
        if i == '.':
            output.append(0)
        elif i == '#':
            output.append(1)
        else:
            output.append(2)
    return output


grid = [parse_line(line) for line in puzzle_input]


def move(position, input_direction):
    x, y = position
    dx, dy = input_direction
    new_x, new_y = x + dx, y + dy
    while (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid)) and grid[new_y][new_x] == 0:
        new_y, new_x = new_y + dy, new_x + dx
    new_y, new_x = new_y - dy, new_x - dx

    grid[y][x] = 0
    grid[new_y][new_x] = 2
    return True


def get_load():
    load = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 2:
                load += len(grid) - y
    return load


def print_grid():
    for row in grid:
        for rock in row:
            if rock == 0:
                print('.', end='')
            elif rock == 1:
                print('#', end='')
            else:
                print('O', end='')
        print('')
    print('')


def tilt_platform(input_direction):
    x_values = range(len(grid[0]))
    y_values = range(len(grid))
    if input_direction in [(0, 1), (1, 0)]:
        x_values = range(len(grid[0]) - 1, -1, -1)
        y_values = range(len(grid) - 1, -1, -1)
    for y_position in y_values:
        for x_position in x_values:
            if grid[y_position][x_position] == 2:
                move((x_position, y_position), input_direction)


tilt_platform((0, -1))
print(get_load())
