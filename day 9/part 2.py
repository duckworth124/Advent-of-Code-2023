import re

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def parse_line(input_line):
    return [int(i) for i in re.findall(r'-?\d+', input_line)][::-1]


def pairs(input_sequence):
    return zip(input_sequence, input_sequence[1:])


def get_difference_sequences(input_sequence):
    output = [input_sequence]
    while not all([i == 0 for i in output[-1]]):
        current_sequence = []
        for current_term, next_term in pairs(output[-1]):
            current_sequence.append(next_term - current_term)
        output.append(current_sequence)
    return output


def extrapolate(input_sequence_with_differences):
    for sequence_index in range(len(input_sequence_with_differences))[::-1]:
        if sequence_index == len(input_sequence_with_differences) - 1:
            input_sequence_with_differences[sequence_index].append(0)
            continue
        input_sequence_with_differences[sequence_index].append(
            input_sequence_with_differences[sequence_index][-1] +
            input_sequence_with_differences[sequence_index + 1][-1]
        )
    return input_sequence_with_differences


total = 0
for line in puzzle_input:
    difference_sequence = get_difference_sequences(parse_line(line))
    difference_sequence_extrapolated = extrapolate(difference_sequence)
    total += difference_sequence_extrapolated[0][-1]
print(total)
