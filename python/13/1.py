import time
start_time = time.time()



def read_file(file_path):
    with open(file_path, "r") as file:
        input_text = file.read()
    return input_text

def parse_rounds(input_text, offsett):
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
            "x": int(target_data[0].split("=")[1]) + offsett,
            "y": int(target_data[1].split("=")[1]) + offsett
        }
        
        rounds.append({"button_a": button_a, "button_b": button_b, "target": target})
    
    return rounds


def solve_round(round):
    button_a = round['button_a']
    button_b = round['button_b']
    target = round['target']
    # 94a + 22b = 8400
    # 34a + 67b = 5400
    ## Ganger den første med 67 på begge sider, den andre med 22 (Verdien for B)
    # 67 ×( 94a + 22b)= 67 × 8400 ==  6298a + 1474b = 562 800
    # 22 x( 34a + 67b)= 22 x 5400 ==  748a + 1474b = 118 800

    # Trekk fra ligning 1 i ligning 2
    # 6298a + 1474b - 748a - 1474b = 
    # 5550a = 444 000 = 80
    
    # Setter inn 80 for A ligning 2
    # 34*80 + 67b = 5400 ==  2720 + 67b = 5400 == 57b = 2680 
    # b = 40
    A1, B1, C1 = button_a['x'], button_b['x'], target['x'] # 94,22,8400
    A2, B2, C2 = button_a['y'], button_b['y'], target['y'] # 34,67,5400
    eq1_multiplied = (A1 * B2, B1 * B2, C1 * B2)  # (6298(a),1474(b),562800)
    eq2_multiplied = (A2 * B1, B2 * B1, C2 * B1)  # (748(a),1474b(b),118800)

    a_coefficient = eq1_multiplied[0] - eq2_multiplied[0] # 6298a - 748a
    b_coefficient = eq1_multiplied[1] - eq2_multiplied[1] # 1474b - 1474b = 0 
    result = eq1_multiplied[2] - eq2_multiplied[2]  # 562800 - 118800

    a = result / a_coefficient # 562 800 - 118 800 
    b = (C1 - A1 * a) / B1 ## b = (8400 - (94 * 80) ) / 22 =  40

    return a, b

total_cost_1 = 0
total_cost_2 = 0
number_of_wins_1 = 0
number_of_wins_2 = 0
input_file = read_file('input.txt')
rounds = parse_rounds(input_file,0)
for i, round in enumerate(rounds, start=1):
    a,b = solve_round(round)
    if a == int(a) and b == int(b):
        total_cost_1 += int(a*3 + b)

rounds2 = parse_rounds(input_file, 10000000000000)
for i, round in enumerate(rounds2, start=1):
    a,b = solve_round(round)
    if a == int(a) and b == int(b):
        total_cost_2 += int(a*3 + b)

print(f"Round 1: Total cost to win {number_of_wins_1} prices: {total_cost_1}") # 35729
print(f"Round 2: Total cost to win {number_of_wins_2} prices: {total_cost_2}") # 88584689879723
end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time_ms} milliseconds")