from collections import defaultdict
import time

def read_file(filename):
    with open(filename) as f:
        input_data = f.read()

    # Convert the input into a list of integers
    data = [int(num) for num in input_data]
    return data
start_time = time.time()

data = read_file('input.txt')

current_position = 0
grid = {}  
gap_positions = defaultdict(list)  

for i, num in enumerate(data):
    if i % 2 == 0:  
        file_id = i // 2
        grid[file_id] = [current_position, num]  
    else:  
        if num > 0:
            gap_positions[num].append(current_position)  
            gap_positions[num].sort()
    current_position += num  



for file_id in sorted(grid.keys(), reverse=True):  
    file_start, file_length = grid[file_id]  
    
    possible_gaps = []
    for gap_length, start_positions in gap_positions.items():
        if gap_length >= file_length:  
            possible_gaps.append([start_positions[0], gap_length]) 
    
    if possible_gaps:  
        possible_gaps.sort()

        gap_start, gap_length = possible_gaps[0]
        
        if file_start > gap_start:  
            grid[file_id] = [gap_start, file_length]  
            
            remaining_gap = gap_length - file_length
            
            gap_positions[gap_length].remove(gap_start)
            
            if not gap_positions[gap_length]: 
                del gap_positions[gap_length]
            
            if remaining_gap > 0:
                new_gap_start = gap_start + file_length  
                if remaining_gap not in gap_positions:
                    gap_positions[remaining_gap] = [] 
                gap_positions[remaining_gap].append(new_gap_start) 
                gap_positions[remaining_gap].sort()  

answer = 0
for file_id, (start, length) in grid.items():
    contribution = start * length + (length * (length - 1)) // 2
    answer += file_id * contribution
end_time = time.time()

print(answer) ## 2858
elapsed_time_ms = (end_time - start_time) * 1000

print(f"Elapsed time: {elapsed_time_ms} milliseconds")