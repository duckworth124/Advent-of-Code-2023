import re
import math

with open('puzzle input.txt', 'r') as f:
    puzzle_input = f.read().split('\n')


def get_number_of_options(total_time, max_distance):
    # roots of x(T-x) - m = -x^2 + Tx - m
    upper_root = (-total_time - (total_time ** 2 - 4 * max_distance) ** 0.5) / -2
    lower_root = (-total_time + (total_time ** 2 - 4 * max_distance) ** 0.5) / -2
    lower_bound = math.ceil(lower_root)
    if lower_root.is_integer():
        lower_bound += 1
    upper_bound = math.floor(upper_root)
    if upper_root.is_integer():
        upper_bound -= 1

    return upper_bound - lower_bound + 1


total_times = [int(i) for i in re.findall(r'\d+', puzzle_input[0])]
max_distances = [int(i) for i in re.findall(r'\d+', puzzle_input[1])]

product = 1
for total_time, max_distance in zip(total_times, max_distances):
    product *= get_number_of_options(total_time, max_distance)
print(product)