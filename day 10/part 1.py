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
distances = [min(i, len(loop) - i) for i in range(len(loop))]
print(max(distances))
