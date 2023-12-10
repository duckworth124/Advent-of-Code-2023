import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    if line[0].isdigit():
        return tuple(re.findall(r'\d+', line))
    match = re.match(r'(\w+)-to-(\w+)', line)
    return match.group(1), match.group(2)


def parse_input():
    maps = {}
    properties = []
    for line in puzzle_input[1:]:
        if line == '':
            continue

        line_parsed = parse_line(line)
        if line_parsed[0].isdigit():
            maps[current_map].append(line_parsed)
            continue
        maps[line_parsed] = []
        current_map = line_parsed
        properties.append(line_parsed[1])
    return maps, properties


def get_location(seed):
    current_property = 'seed'
    current_property_value = seed
    for next_property in properties:
        current_map = puzzle_input_parsed[(current_property, next_property)]
        for destination_start, source_start, length in current_map:
            source_start, destination_start, length = int(source_start), int(destination_start), int(length)
            if source_start <= current_property_value <= source_start + length - 1:
                current_property_value = current_property_value - source_start + destination_start
                break

        current_property = next_property

    return current_property_value


seeds = [int(i) for i in re.findall(r'\d+', puzzle_input[0])]
puzzle_input_parsed, properties = parse_input()

locations = [get_location(seed) for seed in seeds]
print(min(locations))
