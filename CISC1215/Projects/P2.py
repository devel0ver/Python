################################
#Project 3
# CISC 1215
# Points possible : 30 + 10
# Due date: Nov 12th 1 Pm
################################


def print_puzzle(puzzle):
    print("  --  --  --  -- ")
    for x in puzzle:
        print("| "+" | ".join([str(y) for y in x])+" |")
        print("  --  --  --  -- ")
    return None
#################
# 4x4 ken-ken puzzle 
# puzzle_solution: This is the puzzle solution represented as a nested list. 
#              The outer list containts four inner lists each with 4 elements
# constraints_dictionary: This specifies the cage constraints as a dictionary
#                   Keys: Each key in the dictionary specifies the numerical constraint
#                         and the  constraint operator separated by comma. 
#                         Examples:
#                           "4"- 4 is the numerical constraint and there is no constraint operator
#                           "24,*"- 24 is the numerical constraint and the constraint operator is *
#                   Values: Each value is a list of tuples, each tuple is a row column pair. 
#                           The sequence of tuples specifies all the rows and columns on which
#                           the constraint should be met
#                           Examples:
#                                   "4":[(0,0)] - The value on row, column 0,0 should be 4
#                                   "24,*":[(0,1),(0,2),(1,2)] - The product of the values in the specfied 
#                                   rows and columns should be 24
#################
puzzle_solution=[[4,3,2,1],[2,1,4,3],[3,2,1,4],[1,4,3,2]]
# constraints_dictionary={"4":[(0,0)],"24,*":[(0,1),(0,2),(1,2)],"2,/":[(2,3),(3,3)],\
#                         "12,*":[(3,0),(3,1),(3,2)],"2,-":[(0,3),(1,3)],"6,*":[(1,0),(1,1),(2,0)]}
constraints_dictionary={"4":[(0,0)],"24,*":[(0,1),(0,2),(1,2)],"2,/":[(2,1),(2,2)],\
                        "2,/":[(2,3),(3,3)],"12,*":[(3,0),(3,1),(3,2)],"2,-":[(0,3),(1,3)],"6,*":[(1,0),(1,1),(2,0)]}
print_puzzle(puzzle_solution)

########
#Incorrect solutions to evaluate your code
########
incorrect_solution1=[[4,3,2,1],[2,1,4,3],[1,4,3,2],[3,2,1,4]]
incorrect_solution2=[[4,3,2,1],[2,1,4,3],[1,4,3,2],[3,2,1,4]]
incorrect_solution3=[[4,3,2,1],[3,1,4,2],[2,4,1,3],[1,2,3,4]]

###################
# Stage 0: 5 Points
# Obtain a new solution cell-by-cell, there are 16 cells in the 4 x 4 puzzle
# user_input: An input prompt. The input for the cell i, i can take values from 1-16
#           Layout below shows the cell value for each location in the 4 x 4 puzzle
#           You have to convert the each cell value in to its corresponding index based on the layour below
#           Example: 1- (0,0), 2- (0,1), 3-(0,2)
#                --   --   --   -- 
#              | 1  | 2  | 3  | 4  |
#                --   --   --   -- 
#              | 5  | 6  | 7  | 8  |
#                --   --   --   -- 
#              | 9  | 10 | 11 | 12 |
#                --   --   --   -- 
#              | 13 | 14 | 15 | 16 |
#                --   --   --   -- 
# new_puzzle_solution: You will create a nested list obtaining user input for each cell
# Note: You can only use loops for this and the user prompt should be asking values for each cell
######################
new_puzzle_solution=[]

#Write code here
cells = 16
dividend = 1

# As long as dividened sqrd is less that the cells, increment the dividened
# Ex: div = 1, cells = 16, div 1 < cell 16 --> div 2, div 4 < 16 --> div 3, div 9 < 16 --> 4, div 16 < 16?
while dividend ** 2 < cells:
    dividend += 1
# as long i is less than cells, do some code until false
for i in range(1, cells+1):
    puzzle_rows = (i - 1) // dividend # (x,)
    puzzle_cols = (i - 1) % dividend  # (,y)
    # create a variable that will store the user input and convert the input to an int
    user_input = int(input("Please input the value for the cell, ({},{}): ".format(puzzle_rows, puzzle_cols)))
    
    # Check if the column is 0, since every new row starts with the 0th column
    if puzzle_cols == 0:
        # If true, insert the user_input as an list
        new_puzzle_solution.append([user_input])
    else:
        # since the append function adds to the end of an list, we have to
        # keep adding the values into last list inserted until column is 0
        new_puzzle_solution[-1].append(user_input)

# print(new_puzzle_solution)


#######################
# Stage1: 4 Points
# Verify if the provided puzzle only contains value between 1 and 4
# Print an appropriate output message
# Note: Only for-loops and memberships operators are allowed for this.
# Note: Using wile loops will be penalized
#######################


#Write code here
# Create a variable that will store a boolean and set default to True
valid_int = True
# Iterate through the new_puzzle_solution list
for row in new_puzzle_solution:
    # Iterate through the row (elements in new_puzzle_solution)
    for val in row:
        # Check if the values of the row not in the range of 1 to (div+1)
        if val not in range(1, dividend+1):
            # If true, set valid_int to False
            valid_int = False
            break
# If the valid_int is True, then output an success output message
if valid_int:
    print('\nThe grid contains valid integers. All values are in between 1 and 4')
# Else the integers are not valid
else:
    print('\nThe grid does not contain valid integers! Values must be between 1 and 4')
    

###################
# Stage 2: 5 Points
# Verify if the provided puzzle does not repeat the numbers within a row or a column
# Print an appropriate output message
# Note: Only for-loops and the list method count is allowed
# Note: Using wile loops will be penalized
######################

#Write code here
not_repeated = True

# Iterate through the new_puzzle_solution list for the rows
for row in new_puzzle_solution:
    # Iterate through the rows and access the values within them
    for val in row:
        # Check if the count of a value within the row is more than 1
        if row.count(val) > 1:
            not_repeated = False
            
# Iterate through the length of the first index of the list since they all have to have the same length
# Ex: for a 4x4, the length is 4, so from 0-4
for col in range(len(new_puzzle_solution[0])):
    columns = []
    # Iterate through new_puzzle_solution list to access each row
    for row in new_puzzle_solution:
        # print(row[col])
        # We are adding to the columns list the col(index) of each row
        columns.append(row[col])
        # [1,2,3,4]  -> row[0] -> 1
        # [4,3,2,1]  -> row[0] -> 4
        # [3,1,4,2]  -> row[0] -> 3
        # [1,3,2,4]  -> row[0] -> 1
    # Loop through the columns list 
    for val in columns:
        # Check if the count of the value in the columns list is more than 1
        if columns.count(val) > 1:
            not_repeated = False

if not_repeated:
    print("\nPerfect! The puzzle does not repeat numbers within a row or a column")
else:
    print("\nSorry! The puzzle repeats the numbers within a row or a column")

###################
# Stage 3: 7 Points
# Verify if the provided puzzle meets all the cage constraints sepecified in constraint dictionary
# If stage 1 , stage 2, and stage 3 verifications were successful print a congratulatory message
# If a particular cage constraint is not met print the cage constraint that the solution fails
######################


#Write code here

# Initialize a variable type boolean to indicate if met or not
met = True
# set the key and elem global so we can use them outside the for loop
global key, elem
# Iterate through the constraints_dictionary
for key, elem in constraints_dictionary.items():
    # split from the comma, the left is the vale and the right is the operation
    constraint = key.split(',')
    constraint_key_value = int(constraint[0])
    # the puzz_values list will contain the values from the new_puzzle_solution matrix
    # which is accessed by the index of the row and column of the values in the dictionary
    puzz_values = []
    # Iterate through the values corresponding to the key in the dictionary
    for row, col in elem:
        # here is where we add the values to the puzz_values list
        puzz_values.append(new_puzzle_solution[row][col])
    
    # We check if the constraint has an operation or not, if it does than the length is greater than 1
    if len(constraint) > 1:
        # we initialize the operation
        opration = constraint[1]
        # Using if statements to check what type of operation we have as constraint[1]
        if opration == '*':
            total = 1
            for val in puzz_values:
                total *= val
        elif opration == '/':
            total = max(puzz_values) // min(puzz_values)
        elif opration == '+':
            total = sum(puzz_values)
        elif opration == '-':
            total = max(puzz_values) - min(puzz_values)
        
        # I am checking if the calculated total and the constraint_key_value equals to each other
        if total != constraint_key_value:
            # If they dont, that means the condition did not meet and we set met to False
            met = False
            # We initialize the global key and elem so we can use it outside the for loop
            key = key
            elem = elem
            break
        
        # print(f'puzzle_value: {puzz_values}, fixed value: {constraint_key_value}, total: {total}')
    # Otherwise if the key did not have an operation and was an integer by itself instead
    else:
        # Check if the key integer does not equal to the first value in the list, puzz_values
        # Also I need to make sure that the length of puzz_values is not greater than 1 since there is no operations
        if puzz_values[0] != constraint_key_value or len(puzz_values) > 1:
            met = False
        # print(f'puzzle_value: {puzz_values}, fixed value: {constraint_key_value}')
        
print("  --  --  --  --")
for x in new_puzzle_solution:
    print("| "+" | ".join([str(y) for y in x])+" |")
    print("  --  --  --  --")
# If met is True
if met:
    print('The above solution meets all the constraints')
# Otherwise(False),
else:
    # Here I use the global variables, key and elem
    print('\nThe above solution fails cage constraint for {}{}'.format(key, elem))


###################
# Stage 4: 8 Points
# Constraint modification
# constraint_key: User input this will be in the format number,operator example: "12,*"
# constraint_cells: User input this will be a string of numbers separated by comma.: "1,2,3"
#                   The numbers correspond to cell values
#                    You have to convert the each cell value in to its corresponding index refer to stage-0
#                    Example: 1- (0,0), 2- (0,1), 3-(0,2)
# If a constraint is not present in the dictionary you will add it. If it is you will modify it
#Example: If the constrainty "12,*" is not present in constraint_dictionary. 
#         A dictionary item will be created: "12,*":[(0,0),(0,1),(0,2)]
######################

#Write code here
constraint_key = input('Please enter the constraint key (ex. "12,*"): ')
constraint_cells = input('Please enter the constraint cells seperated by comma (ex. "1,2,3"): ')

constraint_cells_list = []
for i in constraint_cells.split(','):
    constraint_cells_list.append(((int(i)-1) // 4, (int(i)-1) % 4))

print('Before updated/new dictionary --> ', constraints_dictionary)
constraints_dictionary[constraint_key] = constraint_cells_list
print('\n\nAfter updated/new dictionary --> ', constraints_dictionary)
################
#Additional 4x4 puzzles: 1 Point
#Please provide two additional puzzle solutions and constraints
#to show that the above code can work for any 4 x4 Kenken puzzle
###############

#Write code here
puzzle_solution = [[5,4,3,2,1],
                   [4,2,1,3,5],
                   [3,1,5,4,2],
                   [2,5,4,1,3], 
                   [1,3,2,5,4]]
additional_constraint = {'40,*':[(0,0), (0,1), (1,1)], '2,/':[(3,2), (4,2)],\
                         '12,+':[(1,3), (1,4), (2,3)], '1,-':[(3,1), (3,2)]}



######################
# [5 points] Extra credit
# Create constraint dictionary from scratch starting with an empty dictionary
# You will provide the following user options as a menu: 
#               1) Add a new constraint
#               2) Change an existing constraint
#               3) Delete an existing constraint
# You will follow the same user input style as in Stage 4 that is constraint_key and constraint_cells             
# Based on the selected option you should decide the user inputs you need to obtain
#Feel free to improvide this implementation as you see fit.
#######################
constraints_dictionary={}
choice = 0

# I am using a while loop so the user can see what they are adding,changing, and deleting.
# They also can add to the dictionary as much as they like, until they quit
while choice != 4:
    print('1) Add a new constraint\
     \n2) Change an existing constraint\
     \n3) Delete an existing constraint\
     \n4) Quit')
    # the variable choice will store the user selection and store it as an integer
    choice = int(input('Choose one of the selection above: '))
    # create an list so that it can store the cells after splitting it and converting it to an int
    constraint_cells_list = []
    # If the user selects 1, then they want to add
    if choice == 1:
        constraint_key = input('Please enter the constraint key (ex. "12,*"): ')
        constraint_cells = input('Please enter the constraint cells seperated by comma (ex. "1,2,3"): ')
        for i in constraint_cells.split(','):
            constraint_cells_list.append(((int(i)-1) // 4, (int(i)-1) % 4))
        constraints_dictionary[constraint_key] = constraint_cells_list
    # Else if the user selects 2, then they want to delete
    elif choice == 2:
        constraint_key = input('Please enter a constraint key you would like to modify: ')
        # Checking if the constraint_key is in the keys of the dictionary
        if constraint_key in constraints_dictionary.keys():
            updated_constraint_cells = input('Please enter the constraint cells: ')
            for i in updated_constraint_cells.split(','):
                constraint_cells_list.append(((int(i)-1) // 4, (int(i)-1) % 4))
            constraints_dictionary[constraint_key] = constraint_cells_list
        # If not exists, the if statement will not execute, instead, the else will
        else:
            print('\nThe constraint key does not exist in the dictionary!')
            print(constraints_dictionary, '\n')
            continue
    # Else if the user selects 3, then they want to update
    elif choice == 3:
        constraint_key = input('Please enter a constraint key you would like to delete: ')
        # Checking if the constraint_key is in the keys of the dictionary
        if constraint_key in constraints_dictionary.keys():
            constraints_dictionary.pop(constraint_key)
            print('\nThe constraint key {} has been removed.'.format(constraint_key))
        # If not exists, the if statement will not execute, instead, the else will
        else:
            print('\nThe constraint key does not exist!')
            print(constraints_dictionary, '\n')
            continue
    else:
        break
    print('-------------------------------------------------------------------')
    print('constraints_dictionary: ', constraints_dictionary, '\n')