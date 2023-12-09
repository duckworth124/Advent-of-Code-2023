with open("puzzle input.txt", "r") as f:
    puzzle_input = f.read().split("\n")


digits = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9'
          }


# does string begin with pattern starting at index?
def check_if_match(string, pattern, index):
    string = string[index:]
    string = string[:len(pattern)]
    return string == pattern


def first_digit(line, from_end=False):
    if from_end:
        line = line[::-1]

    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        for digit in digits:
            pattern = digit
            if from_end:
                pattern = digit[::-1]

            if check_if_match(line, pattern, i):
                return digits[digit]


total = 0
for line in puzzle_input:
    cal = int(first_digit(line) + first_digit(line, from_end=True))
    total += cal

print(total)
