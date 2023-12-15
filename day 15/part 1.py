with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split(',')


def get_hash(input_string):
    output = 0
    for character in input_string:
        output += ord(character)
        output *= 17
        output %= 256
    return output


def main():
    total = 0
    for string in puzzle_input:
        total += get_hash(string)

    print(total)


if __name__ == '__main__':
    main()
