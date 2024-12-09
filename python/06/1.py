def read_map(filename):
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file.readlines()]
    

def find_coordinates(grid, target):
    coordinates = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                coordinates.append((x, y))
                if target == '^':
                    return coordinates
    return coordinates

def get_next_position(position, direction):
    x, y = position
    if direction == "^":  # Up
        return (x, y - 1)
    elif direction == ">":  # Right
        return (x + 1, y)
    elif direction == "v":  # Down
        return (x, y + 1)
    elif direction == "<":  # Left
        return (x - 1, y)
    
def rotate_direction(direction):
    directions = ["^", ">", "v", "<"]
    idx = directions.index(direction)
    return directions[(idx + 1) % 4]


def simulate_trap(grid, obstacles, player_location, state, direction,next_position, visited_cells):
    ## Start by adding a '#' on the next position and then
    new_obstacles = obstacles.copy()
    new_state = state.copy()
    new_obstacles.append(next_position)
    new_visisted_cells = visited_cells.copy()
    t = next_position ## If the allready has moved pass this dont
    if(t in visited_cells):
        return False
    loop = False
    
    while True:
        
        next_position = get_next_position(player_location, direction)
        check_state = (next_position, direction)
        new_visisted_cells.add(next_position)

       
        if(check_state in new_state):
            loop = True
            break
       
        new_state.add(check_state)
        x, y = next_position
        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
            break
        if next_position in new_obstacles:
            direction = rotate_direction(direction)
        else:
            player_location = next_position
    return loop

# Main simulation
def simulate(filename):
    # Load map and initialize
    grid = read_map(filename)
    obstacles = find_coordinates(grid, "#")
    player_location = find_coordinates(grid, "^")[0]
    direction = "^"
    visited_cells = set()
    state = set()
    counter = 0
    number_of_posible_traps = 0

    while True:
        current_state = (player_location, direction)
        counter += 1
        visited_cells.add(player_location)
        state.add(current_state)
        next_position = get_next_position(player_location, direction)
        x, y = next_position
        # Out of bounds = win
        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
            break

        if next_position in obstacles:
            direction = rotate_direction(direction)
        else:
            ## Now we need to simulate if we can get into the same state by adding a # in this cell
            if simulate_trap(grid, obstacles, player_location, state, direction,next_position,visited_cells):
               number_of_posible_traps += 1
           
            player_location = next_position
    return len(visited_cells),number_of_posible_traps
## Sample = 6,1991
# Run the simulation 
filename = "input.txt"
cells_visited,number_of_posible_traps = simulate(filename)
print(f"Part 1: {cells_visited}") # 5239
print(f"Part 2: {number_of_posible_traps}") # 1753 