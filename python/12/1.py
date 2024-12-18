import time
from collections import deque
start_time = time.time()


def read_file(filename):
    data = []
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]
    return data


directions = [
    (-1,0), # Opp
    (0,1), # Høyre
    (1,0), # Ned
    (0,-1) # Venstre
]


part1 = 0
part2 = 0

grid = read_file('input.txt')

rows = len(grid)
columns = len(grid[0])


visited_cords = set()
stopp = False
for row in range(rows):
    for col in range(columns):

        # Skip if visited
        if (row, col) in visited_cords:
            continue

        queue = deque([(row, col)])
        group_area = 0
        group_perimeter = 0
        direction_perimeters = {}
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

            for dy, dx in directions:
                next_row = current_row + dy
                next_col = current_col + dx
                if 0 <= next_row < rows and 0 <= next_col < columns and grid[next_row][next_col] == current_letter:
                   # print("Adding to queue", (next_row,next_col))
                    queue.append((next_row, next_col))
                else:
                    group_perimeter += 1
                    if (dy, dx) not in direction_perimeters:
                        direction_perimeters[(dy, dx)] = set()
                    ## Denne inneholder en liste over alle elementer som har en ukjent Zone i DY,DX retningen
                    #print(direction_perimeters)
                    direction_perimeters[(dy, dx)].add((current_row, current_col))
        # A = 40
        # B = 32
        # C = 40
        # D = 4
        # E = 24
        #print(direction_perimeters)
        part1 += group_area * group_perimeter
        stopp = True
        
        sides = 0
        # current_direction = (-1,0), # Opp(0,1), # Høyre(1,0), # Ned(0,-1) # Venstre
        # coordinates_list = Liste over alle elementer som har en ukjent sone i den retningen
        for current_direction, coordinates_list in direction_perimeters.items():
            # Hvilke noder jeg har besøkt i denne DY,DX 
            visited = set()
           # print(current_direction, coordinates_list)
            for coordinate in coordinates_list:
                if coordinate not in visited:
                    sides += 1
                    
                    queue_to_explore = deque([coordinate])
                    while queue_to_explore:
                        #print("The Queue",queue_to_explore)

                        current_row, current_col = queue_to_explore.popleft()
                        if (current_row, current_col) in visited:
                            #print("been here before?",current_row , current_col)
                            continue ## Next in Queue
                        visited.add((current_row, current_col))
                       # print("visisted", visited)
                        for dy, dx in directions:
                            next_cord = (current_row + dy, current_col + dx)
                            #Hvis neste element også er i listen for denne DY,DX må det være en rett strek mellom og de tilhører samme side
                            if next_cord in coordinates_list:
                                #print("Adding a new number to the QUEUE", next_cord)
                                queue_to_explore.append(next_cord)
           #print("Number of sides!!", sides)
        # A = 4 * 4 = 16
        # B = 4 * 4 = 16
        # C = 4 * 8 = 32
        # D = 1 * 4 = 4
        # E = 3 * 4 = 12
        
       # print(f"{current_letter} Area:{group_area} * Sides:{sides} = Price {group_area*sides}")
        
        part2 += group_area * sides
    
    
    
  

print(part1) ## 140 / 1363682
print(part2) ## 80
end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")