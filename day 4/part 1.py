import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    line = line.split(':')[1]
    winning_numbers, numbers_received = line.split('|')
    winning_numbers = re.findall(r'\d+', winning_numbers)
    numbers_received = re.findall(r'\d+', numbers_received)
    matches = 0
    for number in numbers_received:
        if number in winning_numbers:
            matches += 1

    if matches == 0:
        return 0
    return 2 ** (matches - 1)


total = 0
for line in puzzle_input:
    total+= parse_line(line)
print(total)
