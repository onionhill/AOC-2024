from collections import defaultdict
from itertools import combinations


def read_file(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    
    locations = defaultdict(list)
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                locations[char].append((r, c))
    print(locations)
    return locations, len(grid), len(grid[0])

def part_1(nodes, gridY, gridX):
    antinodes = set()
    
    for positions in nodes.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1

                check_nodes = [
                    (x1 - dx, y1 - dy),  
                    (x2 + dx, y2 + dy),  
                ]

                for r, c in check_nodes:
                    if 0 <= r < gridY and 0 <= c < gridX:
                        antinodes.add((r, c))
    return antinodes


def part_2(nodes, gridY, gridX):
    antinodes = set()
    for positions in nodes.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1

                row, col = x1, y1

                ## Fremover
                row, col = x2, y2
                while 0 <= row < gridY and 0 <= col < gridX:
                    antinodes.add((row, col))
                    row += dx  
                    col += dy  

                # Bakover
                row, col = x1, y1
                while 0 <= row < gridY and 0 <= col < gridX:
                    antinodes.add((row, col))
                    row -= dx
                    col -= dy
    return antinodes


nodes, gridY, gridX = read_file('input.txt')
part1_nodes = part_1(nodes, gridY, gridX)
part2_nodes = part_2(nodes, gridY, gridX)
part2_result = len(part2_nodes)


print(f"Part 1 Solution: {len(part1_nodes)}")
print(f"Part 2 Solution: {len(part2_nodes)}")
