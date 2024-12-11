import time
start_time = time.time()

def read_file(filename):
    data = []
    with open(filename) as file:
        data = [[int(n) for n in line.strip()] for line in file]
    return data

def find_path(grid, y, x, oy, ox, prev_value, paths):
    # Utfor kartet
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return
    # Sjekker om cellen er neste verdi i rekken 1-9
    if grid[y][x] != prev_value + 1:
        return
    # Gyldig rekke. Legger inn slutt kordinatet 
    if grid[y][x] == 9:
        #if (y, x) not in paths[oy, ox]:
        paths[oy, ox].append((y, x))

    directions = [
        (-1, 0),  # Opp
        (0, 1),   # Høyre
        (1, 0),   # Ned
        (0, -1)   # Venstre
    ]

    # Check all 4 directions 
    for dy, dx in directions:
        find_path(grid, y + dy, x + dx, oy, ox, grid[y][x], paths)

data = read_file('input.txt')

paths = {}
for y, row in enumerate(data):
    for x, number in enumerate(row):
        
        if number == 0:
            paths[y, x] = []
            find_path(data, y, x, y, x, -1, paths)

unique_paths = [set(path) for path in paths.values()]
part_1 = sum(len(path) for path in unique_paths)
part_2 = sum(len(path) for path in paths.values() )
print(f"Part 1: {part_1}") # 36 / 624
print(f"Part 2: {part_2}") # 81 

end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")