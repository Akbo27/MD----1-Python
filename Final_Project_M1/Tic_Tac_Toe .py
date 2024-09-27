# Tic_Tac_Toe Game
# Step (1) - Build Board
# Step (2) - currentPlayer Input
# Step (3) - check winnning conditions(3Horizontal, 3Vertical, 2Diagonal)
# Step (4) - Check win, check tie
# Step (5) - Switch Player

board = [ 
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
def playerInput(board):
    while True:
        try:
          inp = int(input("Enter a number between 1 to 9. "))
          if inp >= 1 and inp <= 9 and board[inp-1] == "-":
             board[inp-1] = currentPlayer
             break
          else:
             print("Oops! The number is already taken. Please try again.")
        except ValueError:
             print("Invalid input! Please enter a number between 1 to 9.")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
       winner = board[0]
       return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
         winner = board[3]
         return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
         winner = board[6]
         return True
    return False

def checkVertical(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
       winner = board[0]
       return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
         winner = board[1]
         return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
         winner = board[2]
         return True
    return False

def checkDiagonal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
       winner = board[0]
       return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
         winner = board[2]
         return True
    return False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
       currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin(board):
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board):
       printBoard(board)
       print(f"Yayyyy! The winner is {winner}. ")
       return True

    return False

while gameRunning:
    printBoard(board)            
    playerInput(board)           
    if checkWin(board):
       break               
    checkTie(board)            
    switchPlayer()  