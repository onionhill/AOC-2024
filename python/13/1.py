import time
start_time = time.time()



def read_file(file_path):
    with open(file_path, "r") as file:
        input_text = file.read()
    return input_text

def parse_rounds(input_text, offset):
    # Split the input into blocks
    blocks = input_text.strip().split("\n\n")
    rounds = []
    
    for block in blocks:
        lines = block.splitlines()
        
        # A
        button_a_data = lines[0].split(":")[1].strip().split(", ")
        button_a = {
            "x": int(button_a_data[0].split("+")[1]),
            "y": int(button_a_data[1].split("+")[1])
        }
        
        # B
        button_b_data = lines[1].split(":")[1].strip().split(", ")
        button_b = {
            "x": int(button_b_data[0].split("+")[1]),
            "y": int(button_b_data[1].split("+")[1])
        }
        
        # Target locations
        target_data = lines[2].split(":")[1].strip().split(", ")
        target = {
            "x": int(target_data[0].split("=")[1]) + offset,
            "y": int(target_data[1].split("=")[1]) + offset
        }
        
        rounds.append({"button_a": button_a, "button_b": button_b, "target": target})
    
    return rounds

def solve_round(round):
    min_cost = float("inf")
    best_a_presses, best_b_presses = 0, 0
    button_a = round['button_a']
    button_b = round['button_b']
    button_a_cost = 3
    button_b_cost = 1
    target = round['target']
    
    # 
    for a_presses in range(target['x'] // button_a["x"] + 1):
        
        remaining_x = target['x'] - a_presses * button_a["x"]
        remaining_y = target['y'] - a_presses * button_a["y"]

        
        if remaining_x >= 0 and remaining_y >= 0:
            
            if remaining_x % button_b["x"] == 0 and remaining_y % button_b["y"] == 0:
                b_presses_x = remaining_x // button_b["x"]
                b_presses_y = remaining_y // button_b["y"]

                
                if b_presses_x == b_presses_y:
                    b_presses = b_presses_x
                    total_cost = a_presses * button_a_cost + b_presses * button_b_cost

                    
                    if total_cost < min_cost:
                        min_cost = total_cost
                        best_a_presses, best_b_presses = a_presses, b_presses

    return min_cost, best_a_presses, best_b_presses


total_cost_1 = 0
total_cost_2 = 0
number_of_wins_1 = 0
number_of_wins_2 = 0
rounds_1 = parse_rounds(read_file('input.txt'),0)
rounds_2 = parse_rounds(read_file('input.txt'),10000000000000)
for i, round in enumerate(rounds_1, start=1):
    print(f"Part 1, Problem{i}")
    min_cost, best_a_presses, best_b_presses = solve_round(round)
    if min_cost < float("inf"):
        total_cost_1 += min_cost
        number_of_wins_1 += 1
    #else:
       # print("No solution found.")
print(f"Round 1: Toatl cost to win {number_of_wins_1} prices: {total_cost_1}")

for i, round in enumerate(rounds_2, start=1):
    
    print(f"Part 2, Problem{i}")
    min_cost, best_a_presses, best_b_presses = solve_round(round)
    if min_cost < float("inf"):
        total_cost_2 += min_cost
        number_of_wins_2 += 1
   # else:
       # print("No solution found.")

print(f"Round 2: Toatl cost to win {number_of_wins_2} prices: {total_cost_2}")


