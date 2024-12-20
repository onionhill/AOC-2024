import time
start_time = time.time()

def load_grid(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        grid = [list(line) for line in lines]
    return grid

def get_start_end():
    s = ()
    e = ()
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == 'S':
                s = (y,x)
            if char == 'E':
                e = (y,x)
    return s,e

# Load grid from the input file
grid = load_grid('input.txt')

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1) ]


start,end = get_start_end()

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

def endpoints(coords):
    y,x = coords
    output = set()
    for dy in range(-20,21):
        dy_max = 20-abs(dy)
        for dx in range( -dy_max , dy_max + 1 ):
            if ( y + dy , x + dx) in track:
                output.add(( y + dy , x + dx ))
    return output

def get_distance(a, b):
    total = 0
    for i in range(len(a)):
        difference = abs(a[i] - b[i])
        total += difference
    return total


part_2 = 0
for coords in track:
    potentials = endpoints(coords)
    for othercoords in potentials:
        if track[othercoords]-track[coords]-get_distance(coords,othercoords) >= 100:
            part_2 += 1

print(part_2) #1014683




end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")