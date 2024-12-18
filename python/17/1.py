import time
import re
import copy

def read_file(filename):
    with open(filename) as file:
        file_content = file.read().strip().split("\n\n")
    
    registers_section = file_content[0]  
    registers = [int(x) for x in registers_section.split()[2::3]] 
    
    program_section = file_content[1] 
    program = [int(x) for x in program_section[9:].split(",")] 
    
    return registers, program



# part 1
def run_program(regs, program, onetime=False):
    result = []                                   
    command = 0
    while command < len(program):

        (opcode, operand) = program[command], program[command+1]

        if operand < 4:
            combo = operand
        else: 
            combo = regs[operand-4]


        # adv 
        if opcode == 0:
            regs[0] = regs[0] // (2 ** combo)
        #bxl
        elif opcode == 1: 
            regs[1] = regs[1] ^ operand
        #bst 
        elif opcode == 2: 
            regs[1] = combo % 8
        #jnz
        elif opcode == 3: 
            if regs[0]:
                command = operand - 2
                if onetime:
                    return result
            else:
                command = command
        #bxc
        elif opcode == 4: 
            regs[1] = regs[1] ^ regs[2]
        #out
        elif opcode == 5: 
            result.append( combo % 8  )
        #bdv
        elif opcode == 6:
            regs[1] = regs[0] // (2 ** combo)
        #cdv
        else: 
            regs[2] = regs[0] // (2 ** combo)
        command += 2
    return result



def find_solutions(values, program, a, part_2, level):
    val = values[-level]
    for i in range(0, 8):
        test = run_program([a+i,0,0] , program, True)
        if test[0] == val:
            if level == len(values):
                part_2.append(a+i)
            elif level < len(values):
                find_solutions(values, program, (a+i) * 8, part_2, level+1)


registers,program = read_file("input.txt")
result = run_program(registers,program)
print("Part1: ",result) # [4, 6, 1, 4, 2, 1, 3, 1, 6]

values = copy.deepcopy(program)
part_2 = []
find_solutions(values, program, 0, part_2, 1)
if len(part_2):
    print("pt 2: smallest reg_a:", min(part_2) ) # 202366627359274

