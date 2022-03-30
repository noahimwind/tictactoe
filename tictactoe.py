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

def is_win(user, board):
    if check_row(user, board): return True
    elif check_col(user, board): return True
    elif check_diag(user, board): return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break 
        if complete_row: return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diag(user, board):
    #top left to bottom right
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


#   gameplay    ------------------------------------------------------------------------------------------
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
    if is_taken(coords, board):
        print("please try again")
        continue
    add_to_board(coords, board, active_user)
    if is_win(active_user, board):
        print(f"{active_user} won.")
        break
    user = not user
