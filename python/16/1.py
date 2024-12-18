import sys
from collections import deque
import math

def read_file(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid


def find_start_end(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start,end




def part_1(grid,):
    start, end = find_start_end(grid)
    rows = len(grid) 
    cols = len(grid[0])

    # Initialize an empty list to hold all rows
    dist = []

    # Loop through each row index
    for i in range(rows):
        row = []
        for j in range(cols):
            direction_list = []
            for k in range(4):
                direction_list.append(math.inf)
            row.append(direction_list)
        dist.append(row)

    
    DIRECTIONS = {
        "^": ([">", "<"], (-1, 0)),
        ">": (["v", "^"], (0, 1)),
        "v": (["<", ">"], (1, 0)),
        "<": (["^", "v"], (0, -1)),
    }


    direction_map = [">", "v", "<", "^"]
    q = deque([(start[0], start[1], 0, 0)]) 

    while q:
        y, x, direction_index, move_cost = q.popleft()
        
        # Out of bounds
        if y < 0 or y >= rows or x < 0 or x >= cols or grid[y][x] == '#':
            continue
        
        # Funnet bedre løsning
        if dist[y][x][direction_index] <= move_cost:
            continue
        
        dist[y][x][direction_index] = move_cost
        
        # GOAL!
        if (y, x) == end:
            continue
        
       
        cur_dir = direction_map[direction_index]
        opt, delta = DIRECTIONS[cur_dir]
        
        # Move to the next cell in the current direction
        q.append((y + delta[0], x + delta[1], direction_index, move_cost + 1))

        # Also check for other direction changes
        for new_dir in opt:
            new_d_idx = direction_map.index(new_dir)
            q.append((y, x, new_d_idx, move_cost + 1000))

    print(dist[end[0]][end[1]])
    return min(dist[end[0]][end[1]])




grid = read_file("input.txt")
result = part_1(grid)

print(result) # 94436
