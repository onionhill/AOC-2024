# Open the file and read the input
import time
start_time = time.time()

def read_file(filename):
    data = []
    with open(filename) as file:
        raw_input = file.read()
        for num in raw_input:
            data.append(int(num))
    return data

data = read_file('sample.txt')

data_list = []
for i, num in enumerate(data):
    for dummy in range(num):
        if i % 2 == 0:
            data_list.append(i // 2)  
        else:
            data_list.append(-1) 

while -1 in data_list:
    if data_list[-1] == -1:  
        data_list.pop()  
    else:
        index = data_list.index(-1)
        data_list[index] = data_list.pop()  # Move the last element to the -1 position

# Calculate the answer by summing index multiplied by value
sum = 0

for i, num in enumerate(data_list):
    sum += i * num

# Print the final result
print("Part 1:" , sum)
end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000

print(f"Elapsed time: {elapsed_time_ms} milliseconds")