from collections import deque

def read_file(filename):
    with open(filename, "r") as file:
        obstacles = [line.strip() for line in file.readlines()]
    return obstacles

# BFS
def shortest_path(grid, start, end):
    rows= len(grid)
    cols = len(grid[0])

    queue = deque([(start, [])])
    visited = set([start])

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1) ]

    while queue:
        (y, x), path = queue.popleft()

        if (y, x) == end:
            return path + [(y, x)]

        for dy, dx in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if new_y in range(rows) and new_x in range(cols) and grid[new_y][new_x] == "." and (new_y, new_x) not in visited:
                queue.append(((new_y, new_x), path + [(new_y, new_x)]))
                visited.add((new_y, new_x))

    return None


obstacles = read_file("input.txt")
grid_size =  71 # 7
grid = [['.' for x in range(grid_size)] for y in range(grid_size)]

for i in range(len(obstacles)):
    
    y, x = list(map(int, obstacles[i].split(',')))
    grid[y][x] = "#"
    path = shortest_path(grid, (0, 0), (grid_size - 1, grid_size - 1))

    # no path, obstacles[i] is the blocking obstacle
    if path is None:
        break
print(obstacles[i])