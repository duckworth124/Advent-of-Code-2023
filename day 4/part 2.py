import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(line):
    line = line.split(':')[1]
    winning_numbers, numbers_received = line.split('|')
    winning_numbers = re.findall(r'\d+', winning_numbers)
    numbers_received = re.findall(r'\d+', numbers_received)
    return winning_numbers, numbers_received


def evaluate_card(card):
    winning_numbers, numbers_received = puzzle_input_parsed[card]
    matches = 0
    for number in numbers_received:
        if number in winning_numbers:
            matches += 1

    for i in range(matches):
        i += 1
        collected_cards[card + i] += collected_cards[card]


puzzle_input_parsed = [parse_line(line) for line in puzzle_input]

collected_cards = {}
for i in range(len(puzzle_input)):
    collected_cards[i] = 1

total = 0
for card in range(len(puzzle_input)):
    evaluate_card(card)
    total += collected_cards[card]

print(total)
