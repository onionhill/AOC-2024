with open('input.txt', 'r') as file:
    lines = file.readlines()


sum_safe = 0

for line in lines:
    numbers = line.split()
    prev_number = None
    up = False
    down = False
    safe = True
    for number in numbers:
        number = int(number)
        if prev_number is not None:
            if prev_number == number:
                ## same number == not safe
                safe = False
                break

            if prev_number < number:
                up = True
            if prev_number > number:
                down = True

            if up and down:
                safe = False
                break

            print(number,prev_number)
            diff = abs(prev_number - number)
            
            if diff > 3:
                safe = False
                break
        prev_number = number  
    if safe:
        sum_safe += 1
print(sum_safe)

        
        

