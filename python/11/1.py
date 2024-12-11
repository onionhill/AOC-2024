from collections import defaultdict
import time
start_time = time.time()

def read_file(filename):
    data = []
    with open(filename) as file:
        data = file.readline().strip().split(" ")

    rock_counts = {}
    for rock in data:
        if rock in rock_counts:
            rock_counts[int(rock)] += 1
        else:
            rock_counts[int(rock)] = 1
    return rock_counts


def blink(rock):
    rock_string = str(rock)
    rock_length = len(str(rock))

    if rock == 0:
        return [1]
    elif rock_length % 2 == 0:
        mid = rock_length // 2
        return [int(rock_string[:mid]), int(rock_string[mid:])]
    else:
        return [2024 * rock]




def part1():
    rock_counts = read_file('input.txt')
    for _ in range(25):  
        new_rock_counts = defaultdict(int)
        for rock, count in rock_counts.items():
            for new_rock in blink(rock):
                new_rock_counts[new_rock] += count
        
        rock_counts = new_rock_counts
    return sum(rock_counts.values())



def part2():
    rock_counts = read_file('input.txt')
    for _ in range(75):  
        new_rock_counts = defaultdict(int)
        for rock, count in rock_counts.items():
            for new_rock in blink(rock):
                new_rock_counts[new_rock] += count
        
        rock_counts = new_rock_counts
    return sum(rock_counts.values())



print(f"Part 1: {part1()}") # 218079
print(f"Part 2: {part2()}") # 259755538429618 

end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")
