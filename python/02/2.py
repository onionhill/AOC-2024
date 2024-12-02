

def check_line(numbers):
    
    prev_number = None
    up = False
    down = False
    safe = True
    removeIndex = 0
    for index,number in  enumerate(numbers):          

        if prev_number is not None:
            if prev_number == number:
                ## same number == not safe
                safe = False

            if prev_number < number:
                up = True
            if prev_number > number:
                down = True

            if up and down:
                safe = False

            diff = abs(prev_number - number)
            
            if diff > 3 :
                safe = False
                
            if not safe:
                removeIndex = index
                break
        prev_number = number
    return safe,removeIndex


with open('input.txt', 'r') as file:
    lines = file.readlines()

sum_safe = 0


for line in lines:
    
    numbers = [int(num) for num in line.split()] 
    safe,removeIndex = check_line(numbers)

    if not safe:
        runMore = False
        if removeIndex == 1 or removeIndex == 2:
            ## also check for index = 0
            runMore = True
        new_numb = numbers.copy()
        del new_numb[removeIndex]
        safe, _ = check_line( new_numb)
        
        if not safe and runMore:
            new_numb = numbers.copy()
            del new_numb[removeIndex-1]
            safe, _ = check_line( new_numb)
            
        if not safe and runMore and removeIndex == 2:
            new_numb = numbers.copy()
            del new_numb[removeIndex-2]
            safe, _ = check_line( new_numb)
       
    if safe:
        sum_safe += 1
   

    

print(sum_safe)

        