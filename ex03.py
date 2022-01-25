# EX03
# n-queens problem

Size = 8
  
def print_grid(board): 
    for i in range(Size): 
        for j in range(Size): 
            print (board[i][j], end = " ") 
        print() 
        
def is_possible(board, row, col): 
  
    # Testing the row on the left. No need to test columns, since by choosing to
    # place the queens one column at the time we can implicitly discriminate valid
    # positions
    for i in range(col): 
        if board[row][i] == 'Q': 
            return False
  
    # Testing the upper diagonal side
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 'Q': 
            return False
  
    # Testing the lower diagonal side
    for i, j in zip(range(row, Size, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 'Q': 
            return False
  
    return True
  
def solve(board, col): 
      
    # This will serve as a base case for our recursion. If there is an equal number of 
    # approved rows (or greater) than the Size value, it means that all queens have been placed
    if col >= Size: 
        return True
  
    # Checking one column and testing if each position in the given row is safe for the queen. 
    for i in range(Size): 
  
        if is_possible(board, i, col): 
              
            # The position where the queen can be placed safely
            board[i][col] = 'Q'
  
            # Once the initial queen has been placed, recursion will iterate through col + 1,
            # to check whether further queens can be placed with the assumption of those placed
            # before them, until the base argument is satisfied or solve returns False.
            if solve(board, col + 1) == True: 
                return True
            else:
            # The recursion will backtrack to the previous checkpoint and reassign the value 
            # '.' to the position from which the next test led to a deadend.
                board[i][col] = '.'
  
    return False
  

def solution(): 
    
    board = [['.']*Size for i in range(Size)]
    
    if solve(board, 0) == False: 
        print ("Solution does not exist") 
        return False
  
    else:
        print_grid(board) 
        return True
  
# solution output 
solution() 
  