import time
from collections import deque
start_time = time.time()


def read_file(filename):
    with open(filename) as file:
        data = file.read()

    sections = data.strip().split("\n\n")
    grid = [list(line) for line in sections[0].split("\n")]

    instructions = ''.join(sections[1].split("\n"))

    return grid,instructions


def move_box(x,y, dx, dy):
    next_x = x + dx
    next_y = y + dy

    ## Tomt felt (bytt plass)
    if grid[next_y][next_x] == ".":
        grid[next_y][next_x] = grid[y][x]
        grid[y][x] = '.'
        return True
    ## Vegg, stopp
    elif grid[next_y][next_x] == "#":
        return False
    ## Boks, sjekk om den kan flyttes
    else:
        if(move_box(next_x, next_y, dx,dy) ):
            current_value = grid[y][x]
            next_value = grid[next_y][next_x]
            
            grid[y][x] = next_value
            grid[next_y][next_x] = current_value
            return True



DIRECTIONS = {
    "^": {"x": 0, "y": -1},
    ">": {"x": 1, "y": 0},
    "v": {"x": 0, "y": 1},
    "<": {"x": -1, "y": 0},
}

grid,instructions = read_file('input.txt')

start = {}
found_start = False
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "@":
            start = {"x": x, "y": y}
            grid[y][x] = "."
            found_start = True
            break
    if found_start:
        break

for instruction in instructions:
    direction = DIRECTIONS[instruction]
    current_position = {"x": start["x"] + direction["x"], "y": start["y"] + direction["y"]}

    ##Vegg == Next
    if grid[current_position["y"]][current_position["x"]] == "#":
        continue
 
    ## Tomt == Flytt uten å gjøre noe mer
    if grid[current_position["y"]][current_position["x"]] == ".":
        start = current_position
        continue

    ## Boks
    if grid[current_position["y"]][current_position["x"]] == "O" and move_box( current_position["x"], current_position["y"], direction["x"], direction["y"] ):
        start = current_position
        continue
   

score = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "O":
            score += (y * 100) + x

print(score) # 10092 / 1457740
 
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")