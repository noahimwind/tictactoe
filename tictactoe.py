# tic tac toe program

#board with 3 lists inside of one list
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user = True #True = x, False = o

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end = "")
        print("\n")

def check_input(user_input):
    #check if it is a number
    if not is_number(user_input): return False
    #check if it is 1 - 9
    user_input = int(user_input)
    if not is_validnumber(user_input): return False
    return True

def is_number(user_input):
    if not user_input.isnumeric():
        print("not a number")
        return False
    else: 
        return True

def is_validnumber(user_input):
    if user_input > 9 or user_input < 1:
        print("number is not valid")
        return False
    else: 
        return True

def is_taken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("already taken")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row, col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

#quit
def quit(user_input):
    if user_input == "q": return True
    else: 
        return False     

def current_user(user):
    if user: return "x"
    else: return "o"

while True:
    active_user = current_user(user)
    print_board(board)
    user_input = input("please enter position 1 - 9 or enter q to quit: ")
    if quit(user_input): break
    if not check_input(user_input):
        print("try again")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    #board[0][0] = "x"
    if is_taken(coords, board):
        print("please try again")
        continue
    add_to_board(coords, board, active_user)
    user = not user
