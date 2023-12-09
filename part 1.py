with open("puzzle input.txt", "r") as f:
    puzzle_input = f.read().split("\n")


def first_digit(line):
    for i in line:
        if i.isdigit():
            return i
    raise Exception


def last_digit(line):
    return first_digit(line[::-1])


total = 0
for line in puzzle_input:
    cal = int(first_digit(line) + last_digit(line))
    total += cal

print(total)
