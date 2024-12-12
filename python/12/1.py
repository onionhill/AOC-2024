import sys
from collections import deque


def read_file(filename):
    data = []
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    return data


directions = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]


part1 = 0
part2 = 0

grid = read_file('small-sample.txt')

rows = len(grid)
columns = len(grid[0])


visited_cords = set()

for row in range(rows):
    for col in range(columns):

        # Skip if visited
        if (row, col) in visited_cords:
            continue

        queue = deque([(row, col)])
        group_area = 0
        group_perimeter = 0
        current_letter = ''
        # BFS 
        while queue:
            current_row, current_col = queue.popleft()
            current_letter = grid[current_row][current_col]
            # Skip if already visited
            if (current_row, current_col) in visited_cords:
                continue

            visited_cords.add((current_row, current_col))
            group_area += 1

            for dr, dc in directions:
                next_row = current_row + dr
                next_col = current_col + dc

                if 0 <= next_row < rows and 0 <= next_col < columns and grid[next_row][next_col] == current_letter:
                    queue.append((next_row, next_col))
                else:
                    group_perimeter += 1
        # A = 40
        # B = 32
        # C = 40
        # D = 4
        # E = 24
        print(current_letter, (group_area * group_perimeter))
        part1 += group_area * group_perimeter
        
  

print(part1) ## 140 / 1363682
