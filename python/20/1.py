import time
start_time = time.time()


def read_file(filename):
    with open(filename) as file:
        grid = file.readlines()
    return grid

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1) ]

grid = read_file("input.txt")
start = ()
end = ()
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'S':
            start = (y,x)
        if char == 'E':
            end = (y,x)


track = {start:0}
cur = start
curstep = 0
while cur != end:
    curstep += 1
    y,x = cur
    for dy,dx in DIRECTIONS:
        new_y = y + dy
        new_x = x + dx
        if (new_y,new_x) not in track and grid[new_y][new_x] in 'SE.':
            cur = (new_y,new_x)
            track[cur] = curstep
            break

count = 0
for y,x in track:
    for dy,dx in DIRECTIONS:
        current_pos = (y, x)
        next_pos = (y + dy, x + dx)
        next_next_pos = (y + 2 * dy, x + 2 * dx)

        if next_pos not in track and next_next_pos in track and track[next_next_pos] - track[current_pos] >= 101:
            count += 1
print(f"Part 1: {count} ") #1417




end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")