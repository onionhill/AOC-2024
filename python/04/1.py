
def read_file_to_array(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]
    
def find_rest_of_word(grid, word, start_row, start_col, dir_row, dir_col):
    # Check for the word in the given direction
    for i in range(len(word)):
        check_row = start_row + (i * dir_row)
        check_col = start_col + (i * dir_col)

        if check_row < 0 or check_row >= len(grid) or check_col < 0 or check_col >= len(grid[0]):
            ## Out of bounds
            return False
        if grid[check_row][check_col] != word[i]:
            ## Word not matching
            return False
        
    return True

def check_cross(grid, start_row,start_col, directions):
    
    word = ['M','S']
    for direction in directions:
        ## Check that both values are the same
        v = []
        for dr, dc in direction:
            check_row = start_row + dr
            check_col = start_col + dc
            if check_row < 0 or check_row >= len(grid) or check_col < 0 or check_col >= len(grid[0]):
                ## Out of bounds
                return False
            v.append(grid[check_row][check_col])
        if v[0] == v[1]:
            return False
        if v[0] not in word or v[1] not in word:
            ## Letters not found
            return False
  
    return True

def find_letter(grid, letter,directions, word ):
    
    rows, cols = len(grid), len(grid[0])
    results = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == letter:
                if letter == 'X':
                    for dr, dc in directions:
                        if find_rest_of_word(grid, word, row, col, dr, dc):
                            results.append((row, col, dr, dc))
                else:
                    if check_cross(grid, row, col, directions):
                        results.append((row, col, directions))

    return results

def main():
    filename = 'input.txt' 
    grid = read_file_to_array(filename)

    
    part_1_matches = find_letter(grid, 'X', [(-1, 0), (1, 0), (0, -1), (0, 1),  (-1, -1), (-1, 1), (1, -1), (1, 1) ], 'XMAS') 
    print("Part 1: " , len(part_1_matches) )
    part_2_matches = find_letter(grid, 'A', [ [(-1, -1),  (1, 1)], [(1, -1), (-1, 1)] ], 'MAS') 
    print("Part 2: " , len(part_2_matches) )



if __name__ == "__main__":
    main()