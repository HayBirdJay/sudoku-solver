# Convert Input to List
def Convert(string):
    li = list(string.split(" "))
    return li

# User's Inputed Board
row1_lst = Convert(input("Insert your own board by putting numbers in\n from left to right with no commas starting Row 1: "))
row2_lst = Convert(input("Row 2: "))
row3_lst = Convert(input("Row 3: "))
row4_lst = Convert(input("Row 4: "))
row5_lst = Convert(input("Row 5: "))
row6_lst = Convert(input("Row 6: "))
row7_lst = Convert(input("Row 7: "))
row8_lst = Convert(input("Row 8: "))
row9_lst = Convert(input("Row 9: "))

board = [row1_lst, row2_lst, row3_lst, row4_lst, row5_lst, row6_lst, row7_lst, row8_lst, row9_lst]

# Create Board Display
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i !=0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print (" | ", end="")
            
            if j == 8:
                 print(bo[i][j])
            else:
                 print(str(bo[i][j]) + " ", end="")

# Solved (Filled) the Board
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

# Try All Numbers
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

# Check If Invalid Number Entry
def valid(bo, num, pos):
    # Check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check Column
    for i  in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    #Create Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #Check Box
    for i in range(box_y*3, box_y*3 + 3):
     for j in range(box_x*3, box_x*3 + 3):
        if bo[i][j] == num and (i,j) != pos:
            return False
   
    return True

# Find Empty Space
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, column
    
    return None

# Check if Board is Correct Then Solve
def check_correct(): 
    answer_correct = input("Is this your board? True/False")
    if answer_correct == "True":
        solve(board)
        print("                                                     ")
        print_board(board)
        
    if answer_correct == "False":
        print("Please start over program and try again")
        
    else:
        print("True/False ")
        check_correct()

print("                                                     ")
print_board(board)
check_correct()
