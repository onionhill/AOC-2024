import sys
from collections import deque
import math
import time
start_time = time.time()


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


def part_2(grid):
    start,end = find_start_end(grid)
    values = []
    rows = len(grid) 
    cols = len(grid[0])

    for y in range(rows):
        values.append([])
        for x in range(cols):
            values[y].append(
                {
                    ">":(math.inf, set()),
                    "v":(math.inf, set()),
                    "<":(math.inf, set()),
                    "^":(math.inf, set())
                }
            )
    q = deque([(*start, ">", 0, set([start]))])
    
    DIRECTIONS = {
        "^": ([">", "<"], (-1, 0)),
        ">": (["v", "^"], (0, 1)),
        "v": (["<", ">"], (1, 0)),
        "<": (["^", "v"], (0, -1)),
    }

   # print(q)
    while q:
        y, x, direction_index, move_cost, path = q.popleft()

        # Out of bounds
        if y < 0 or y >= rows or x < 0 or x >= cols or grid[y][x] == '#':
            continue
        
        path.add((y,x))
        currentMin, currentPath = values[y][x][direction_index]
        if currentMin < move_cost:
            continue
        elif currentMin == move_cost:
            currentPath.update(path)
        else:
            currentPath.clear()
            currentPath.update(path)
            values[y][x][direction_index]=(move_cost, currentPath)

        # GOAL!
        if (y,x) == end:
            continue
        opt, delta = DIRECTIONS[direction_index]

        q.append([y+delta[0], x+delta[1], direction_index, move_cost+1, set(path)])

        for new_direction in opt:
            q.append([y,x,new_direction,move_cost+1000, set(path)])
    return values[end[0]][end[1]]


grid = read_file("input.txt")

score = part_2(grid)
min_path = 0
minscore = math.inf
for _,v in score.items():
    path_score,path = v
    print(path_score, len(path))
    if path_score < minscore:
        min_path = path
        minscore=path_score
print(len(min_path)) # 45
         
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")