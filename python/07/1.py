from operator import add, mul

def read_file(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            target = int(parts[0][:-1])  
            values = list(map(int, parts[1:]))  
            data.append((target, values))
    return data

def concat(x, y):
    return int(str(x) + str(y))

def brute_force(operators):
    total_sum = 0
    data = read_file('sample.txt')

    for target, values in data:
        num_values = len(values)
        num_operators = len(operators)

        for combination_index in range(num_operators ** (num_values - 1)):
            current_value = values[0]
            temp_index = combination_index

            for i in range(1, num_values):
                operator_index = temp_index % num_operators
                temp_index = temp_index // num_operators
                current_operator = operators[operator_index]
                current_value = current_operator(current_value, values[i])

            if current_value == target:
                total_sum += target
                break 
    return total_sum

print("Part 1:", brute_force([add, mul])) # 663613490587
print("Part 2:", brute_force([add, mul, concat])) # 110365987435001
