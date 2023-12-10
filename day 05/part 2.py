import re
import itertools

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


# returns the 3 numbers present if it's a number line, and returns the 2 words in the map if it's a map line
def parse_line(line):
    if line[0].isdigit():
        return tuple(re.findall(r'\d+', line))
    match = re.match(r'(\w+)-to-(\w+)', line)
    return match.group(1), match.group(2)


# generates maps and properties, a dictionary representing all the possible maps and a list of all the
# properties we need to calculate the value of in order
def parse_input():
    maps = {}
    properties = []
    current_map = None
    for line in puzzle_input[1:]:
        if line == '':
            continue

        line_parsed = parse_line(line)
        if line_parsed[0].isdigit():
            line_parsed = tuple([int(i) for i in line_parsed])
            maps[current_map].append(line_parsed)
            continue
        maps[line_parsed] = []
        current_map = line_parsed
        properties.append(line_parsed[1])
    return maps, properties


# takes in a list of ranges of values the current property can have, and applies the mapping rule to output a range of
# values the next property can have as a result
def get_next_property_values(ranges_to_process, current_map):
    output = []
    while ranges_to_process:
        current_start, current_end = ranges_to_process.pop()
        if current_end <= current_start:
            continue

        does_not_intersect_with_any_map = True
        # checks if the current range intersects with one of the maps, and if so, splits the range into 3 parts:
        # the part before the map, the part inside the map, and the part after. it then processes the part inside the
        # map and adds the before and after parts to the queue to be processed separately
        for destination_start, source_start, map_length in puzzle_input_parsed[current_map]:
            source_end = source_start + map_length
            intersection_start = max(source_start, current_start)
            intersection_end = min(source_end, current_end)
            if intersection_end > intersection_start:
                does_not_intersect_with_any_map = False
                output.append((intersection_start - source_start + destination_start,
                               intersection_end - source_start + destination_start))
                ranges_to_process.append((current_start, intersection_start))
                ranges_to_process.append((intersection_end, current_end))
                break

        if does_not_intersect_with_any_map:
            # if a particular range does not intersect with a map, then it is mapped to itself
            output.append((current_start, current_end))

    return output


def is_intersecting(start1, start2, end1, end2):
    return start1 < end2 and start2 < end1


puzzle_input_parsed, properties = parse_input()
seed_matches = re.findall(r'(\d+) (\d+)', puzzle_input[0])
seeds = []
for start, length in seed_matches:
    start, length = int(start), int(length)
    seeds.append((start, start + length))

current_property_values = seeds
for current_map in zip(['seed'] + properties, properties):
    current_property_values = get_next_property_values(current_property_values, current_map)

print(min([i[0] for i in current_property_values]))
