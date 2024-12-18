import time
import re
from itertools import count
from math import prod
start_time = time.time()


def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

    matches = re.findall(pattern, data)
    
    # Convert the matches to a list of integers
    result = []
    for match in matches:
        result.append([int(number) for number in match])
    
    return result

ROBOTS = read_file('input.txt')

X_Size = 103
Y_Size = 101


def step(robot, time):
    y = robot[0]
    x = robot[1]
    dy = robot[2]
    dx = robot[3]

    delta_x = dx * time
    delta_y = dy * time
    new_x = (x + delta_x) % X_Size
    new_y = (y + delta_y) % Y_Size

    return new_x, new_y


def part_one():
    quadrants = [0] * 4

    new_pos = []
    for robot in ROBOTS:
        new_pos.append(step(robot, 100))

    for x, y in new_pos:
        half_x = (X_Size // 2) + 1
        half_y = (Y_Size // 2) + 1

        # Index er 0 eller 1
        x_index, x_remainder = divmod(x, half_x) 
        y_index, y_remainder = divmod(y, half_y) 
        if x_remainder == half_x - 1 or y_remainder == half_y - 1:
            continue

        quadrant_index = x_index * 2 + y_index
        quadrants[quadrant_index] += 1
    ## 125*119*111*135
    return prod(quadrants)

## LOL
def part_two():
     for t in count():
        current_positions = set()
        for robot in ROBOTS:
            current_positions.add(step(robot, t))

        if len(current_positions) == len(ROBOTS):
            return t


print(f"Part 1: {part_one()}") # 222901875
print(f"Part 2: {part_two()}") # 6243

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")