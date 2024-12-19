import time
from functools import lru_cache

start_time = time.time()

def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    patterns = lines[0].strip().split(", ")  
    designs = [line.strip() for line in lines[2:]]  

    return patterns, designs


patterns, designs = read_file("input.txt")

@lru_cache(None)  # Cache results to avoid redundant calculations

def count_combinations(design):
    
    if not design:
        return 1

    total_combinations = 0
    for pattern in patterns:
        if design.startswith(pattern): 
            remaining_design = design[len(pattern):]
            total_combinations += count_combinations(remaining_design)

    return total_combinations

combinations = []
for design in designs:
    combinations.append(count_combinations(design))


part_1_result = 0
for combo in combinations:
    if combo > 0:  # Check if the combination count is greater than 0
        part_1_result += 1

# Part 2: Calculate the total number of combinations for all designs
part_2_result = sum(combinations)

# Print the results
print("1:", part_1_result)
print("2:", part_2_result)




end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")