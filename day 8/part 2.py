import itertools
import re
import math

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    return re.findall(r'\w+', line)


# fast mode assumes the puzzle input has some extra constraints, which it shouldn't necessarily have, but does for some
# reason
def find_cycle(start_pos, fast_mode=False):
    time = 0
    previous_states = [(start_pos, 0)]
    current_pos = start_pos
    goal_times = []
    cycle_start, cycle_length = 0, 0
    for direction in itertools.cycle(directions):
        current_pos = paths[current_pos][direction]
        time += 1

        if not fast_mode:
            current_state = (current_pos, time % len(directions))
            if current_state in previous_states:
                cycle_start = previous_states.index(current_state)
                cycle_length = time - cycle_start
                break
            previous_states.append(current_state)

        if current_pos[-1] == 'Z':
            goal_times.append(time)
            if fast_mode:
                return goal_times, time, time
    return goal_times, cycle_start, cycle_length


def get_cycle_intersection(cycle1, cycle2):
    goal_times1, cycle_start1, cycle_length1 = cycle1
    goal_times2, cycle_start2, cycle_length2 = cycle2
    cycle_length_intersection = math.lcm(cycle_length1, cycle_length2)
    cycle_start_intersection = max(cycle_start1, cycle_start2)

    goal_times_intersection = []
    for goal_time in goal_times1:
        if goal_time < cycle_start1:
            if goal_time in goal_times2:
                goal_times_intersection.append(goal_time)
            continue
        for cycle_count in range(cycle_length_intersection // cycle_length1):
            goal_time_adjusted = goal_time + cycle_count * cycle_length1
            if goal_time_adjusted >= cycle_start2:
                goal_time_adjusted = (goal_time_adjusted - cycle_start2) % cycle_length2 + cycle_start2
            if goal_time_adjusted in goal_times2:
                goal_times_intersection.append(goal_time + cycle_count * cycle_length1)
    return goal_times_intersection, cycle_start_intersection, cycle_length_intersection


directions = puzzle_input[0]
paths = {}
for line in puzzle_input[2:]:
    pos, left, right = parse_line(line)
    paths[pos] = {'L': left, 'R': right}

start_positions = [i for i in paths.keys() if i[-1] == 'A']
cycles = [find_cycle(i, fast_mode=True) for i in start_positions]
print('all cycles processed')
overall_cycle = cycles[0]
for cycle in cycles:
    overall_cycle = get_cycle_intersection(overall_cycle, cycle)
print(overall_cycle[0][0])
