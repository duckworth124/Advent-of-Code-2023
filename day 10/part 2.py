with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')
DIRECTIONS = [(0, 1),
              (0, -1),
              (1, 0),
              (-1, 0)]


def move(pos, direction):
    x, y = pos
    dx, dy = direction
    return x + dx, y + dy


def find_start():
    for row_index, row in enumerate(puzzle_input):
        if 'S' in row:
            return row.index('S'), row_index


def get_next(prev_pos, current_pos):
    next_positions = [next_pos for next_pos in [move(current_pos, direction) for direction in DIRECTIONS]
                      if is_pointing_to(current_pos, next_pos)]
    next_positions.remove(prev_pos)
    if len(next_positions) != 1:
        raise Exception
    return next_positions[0]


def create_loop():
    start = find_start()
    output = {start}
    for direction in DIRECTIONS:
        next_pos = move(start, direction)
        if is_pointing_to(next_pos, start):
            break
    else:
        raise Exception
    current_pos = start
    while next_pos != start:
        output.add(next_pos)
        current_pos, next_pos = next_pos, get_next(current_pos, next_pos)
    return output


# check if from_pos is pointing to to_pos, not necessarily the other way around
def is_pointing_to(from_pos, to_pos):
    from_x, from_y = from_pos
    to_x, to_y = to_pos
    change_x, change_y = to_x - from_x, to_y - from_y
    pipe_from = puzzle_input[from_y][from_x]
    if (change_x, change_y) == (0, -1):
        return pipe_from in ('|', 'J', 'L')
    if (change_x, change_y) == (0, 1):
        return pipe_from in ('|', 'F', '7')
    if (change_x, change_y) == (1, 0):
        return pipe_from in ('L', 'F', '-')
    if (change_x, change_y) == (-1, 0):
        return pipe_from in ('J', '-', '7')
    raise Exception


loop = create_loop()


# for part 2 I'm working with a new coordinate system which is 3 times bigger than the old one in each direction
# this allows us to use normal bfs while allowing for behaviour like 'squeezing between pipes'
# FJL ->
# ....0..0.
# .0000..00
# .0.......
# also, we can safely assume that S is a + shape, as it only has 2 pipes pointing at it
def is_blocked(pos):
    x, y = pos
    if (x // 3, y // 3) not in loop:
        return False

    pipe = puzzle_input[y // 3][x // 3]
    rel_x, rel_y = x % 3, y % 3
    if rel_x != 1 and rel_y != 1:
        return False

    rel_pos = (rel_x, rel_y)
    if pipe == '|':
        return rel_pos in [(1, 0), (1, 1), (1, 2)]
    if pipe == '-':
        return rel_pos in [(0, 1), (1, 1), (2, 1)]
    if pipe == 'L':
        return rel_pos in [(1, 0), (1, 1), (2, 1)]
    if pipe == 'J':
        return rel_pos in [(1, 0), (1, 1), (0, 1)]
    if pipe == 'F':
        return rel_pos in [(2, 1), (1, 1), (1, 2)]
    if pipe == '7':
        return rel_pos in [(0, 1), (1, 1), (1, 2)]
    if pipe == 'S':
        return rel_x == 1 or rel_y == 1


def bfs():
    external_points = [[False for i in range(len(puzzle_input[0]) * 3)] for j in range(len(puzzle_input) * 3)]
    explored_points = [[False for i in range(len(puzzle_input[0]) * 3)] for j in range(len(puzzle_input) * 3)]
    frontier = [(0, 0)]
    while frontier:
        current_pos = frontier.pop()
        for next_pos in [move(current_pos, direction) for direction in DIRECTIONS]:
            next_x, next_y = next_pos
            if not (0 <= next_x < 3 * len(puzzle_input[0]) and 0 <= next_y < 3 * len(puzzle_input)):
                continue
            if explored_points[next_y][next_x]:
                continue
            explored_points[next_y][next_x] = True
            if is_blocked(next_pos):
                continue
            frontier.append(next_pos)
            external_points[next_y][next_x] = True

    return external_points


def get_area(external_points, print_map=False):
    area = 0
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[0])):
            if not ((x, y) in loop or external_points[y * 3][x * 3]):
                area += 1
                if print_map:
                    print('I', end='')
            else:
                if print_map:
                    if (x, y) in loop:
                        print(puzzle_input[y][x], end='')
                    else:
                        print('O', end='')
        if print_map:
            print('')
    return area


print(get_area(bfs(), print_map=True))
