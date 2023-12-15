with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split(',')


def get_hash(input_string):
    output = 0
    for character in input_string:
        output += ord(character)
        output *= 17
        output %= 256
    return output


boxes = [[] for i in range(256)]


def perform_hashmap(input_string):
    if '=' in input_string:
        input_label, input_focal_length = input_string.split('=')
        input_focal_length = int(input_focal_length)
        string_hash = get_hash(input_label)
        for index, (label, focal_length) in enumerate(boxes[string_hash]):
            if label == input_label:
                boxes[string_hash][index] = (input_label, input_focal_length)
                break
        else:
            boxes[string_hash].append((input_label, input_focal_length))

    elif '-' in input_string:
        input_label = input_string[:-1]
        string_hash = get_hash(input_label)
        for index, (label, focal_length) in enumerate(boxes[string_hash]):
            if label == input_label:
                boxes[string_hash].pop(index)

    else:
        raise Exception(input_string)


def get_total_focusing_power():
    total = 0
    for box_index, box in enumerate(boxes):
        box_index += 1
        for lens_index, (label, focal_length) in enumerate(box):
            lens_index += 1
            focal_length = int(focal_length)
            total += box_index * lens_index * focal_length
    return total


def main():
    for instruction in puzzle_input:
        perform_hashmap(instruction)
    print(get_total_focusing_power())


main()
