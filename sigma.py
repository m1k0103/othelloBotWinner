import random

# Create an empty board
def empty_board():
    return [
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_"],
            ]

# Create the starting othello board
def starting_board():
    state = empty_board()
    state[3][3] = "W"
    state[4][4] = "W"
    state[3][4] = "B"
    state[4][3] = "B"
    return state

# Print the board state to console
def print_board(state):
    for row in state:
        print(" ".join(row))

# Return the opposite player of the one provided as input
def opposite(player):
    if player == "B":
        return "W"
    else:
        return "B"

# Check if the game is over, either because the board is full or because one player got eliminated
def game_over(state):
    saw_white = False
    saw_black = False
    for row in state:
        for cell in row:
            if cell == "_":
                return False
            if cell == "W":
                saw_white = True
            if cell == "B":
                saw_black = True
    if not saw_white:
        return True
    if not saw_black:
        return True
    return True

# Calculate scores for the two players, returns a list with black score and white score
def count_scores(state):
    white = 0
    black = 0
    for row in state:
        for cell in row:
            if cell == "W":
                white += 1
            if cell == "B":
                black += 1
    return [black, white]

# Check if placing the disk in a cell will result in disks being flipped below. Assumes coordinates are valid and the cell is empty.
def move_down_valid(state, row, col, player):
    opposite_player = opposite(player)
    if row < 6:
        saw_opposite = False
        for y in range(row + 1, 8, 1):
            if state[y][col] == "_":
                break
            if state[y][col] == opposite_player:
                saw_opposite = True
            if state[y][col] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped above. Assumes coordinates are valid and the cell is empty.
def move_up_valid(state, row, col, player):
    opposite_player = opposite(player)
    if row > 1:
        saw_opposite = False
        for y in range(row - 1, -1, -1):
            if state[y][col] == "_":
                break
            if state[y][col] == opposite_player:
                saw_opposite = True
            if state[y][col] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped on the left. Assumes coordinates are valid and the cell is empty.
def move_left_valid(state, row, col, player):
    opposite_player = opposite(player)
    if col > 1:
        saw_opposite = False
        for x in range(col - 1, -1, -1):
            if state[row][x] == "_":
                break
            if state[row][x] == opposite_player:
                saw_opposite = True
            if state[row][x] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped on the right. Assumes coordinates are valid and the cell is empty.
def move_right_valid(state, row, col, player):
    opposite_player = opposite(player)
    if col < 6:
        saw_opposite = False
        for x in range(col + 1, 8, 1):
            if state[row][x] == "_":
                break
            if state[row][x] == opposite_player:
                saw_opposite = True
            if state[row][x] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped in the up-left direction. Assumes coordinates are valid and the cell is empty.
def move_up_left_valid(state, row, col, player):
    opposite_player = opposite(player)
    if row > 1 and col > 1:
        saw_opposite = False
        for diff in range(1, 8, 1):
            if row - diff < 0 or col - diff < 0:
                break
            if state[row - diff][col - diff] == "_":
                break
            if state[row - diff][col - diff] == opposite_player:
                saw_opposite = True
            if state[row - diff][col - diff] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped in the up-right direction. Assumes coordinates are valid and the cell is empty.
def move_up_right_valid(state, row, col, player):
    opposite_player = opposite(player)
    if row > 1 and col < 6:
        saw_opposite = False
        for diff in range(1, 8, 1):
            if row - diff < 0 or col + diff > 7:
                break
            if state[row - diff][col + diff] == "_":
                break
            if state[row - diff][col + diff] == opposite_player:
                saw_opposite = True
            if state[row - diff][col + diff] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped in the down-left direction. Assumes coordinates are valid and the cell is empty.
def move_down_left_valid(state, row, col, player):
    opposite_player = opposite(player)
    if row < 6 and col > 1:
        saw_opposite = False
        for diff in range(1, 8, 1):
            if row + diff > 7 or col - diff < 0:
                break
            if state[row + diff][col - diff] == "_":
                break
            if state[row + diff][col - diff] == opposite_player:
                saw_opposite = True
            if state[row + diff][col - diff] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Check if placing the disk in a cell will result in disks being flipped in the down-right direction. Assumes coordinates are valid and the cell is empty.
def move_down_right_valid(state, row, col, player):
    opposite_player = opposite(player)
    if row < 6 and col < 6:
        saw_opposite = False
        for diff in range(1, 8, 1):
            if row + diff > 7 or col + diff > 7:
                break
            if state[row + diff][col + diff] == "_":
                break
            if state[row + diff][col + diff] == opposite_player:
                saw_opposite = True
            if state[row + diff][col + diff] == player:
                if saw_opposite:
                    return True
                else:
                    break
    return False

# Checks if the proposed move is valid
def valid_move(state, row, col, player):
    # Out of bounds moves are invalid
    if row < 0 or row >= 8 or col < 0 or col >= 8:
        return False
   
    # If the cell is occupied, move is invalid
    if state[row][col] != "_":
        return False
   
    if move_down_valid(state, row, col, player):
        return True
   
    if move_up_valid(state, row, col, player):
        return True
   
    if move_left_valid(state, row, col, player):
        return True
   
    if move_right_valid(state, row, col, player):
        return True
   
    if move_up_left_valid(state, row, col, player):
        return True
   
    if move_up_right_valid(state, row, col, player):
        return True
   
    if move_down_left_valid(state, row, col, player):
        return True
   
    if move_down_right_valid(state, row, col, player):
        return True
   
    return False

# Checks if the player has a valid move
def has_valid_move(state, player):
    for row in range(0, 8):
        for col in range(0, 8):
            if valid_move(state, row, col, player):
                return True
    return False

# Returns a list of all valid moves for a player
def list_valid_moves(state, player):
    valid_moves = []
    for row in range(0, 8):
        for col in range(0, 8):
            if valid_move(state, row, col, player):
                valid_moves.append([row, col])
    return valid_moves

def copy_state(state):
    return [row[:] for row in state]

# Returns a copy of the board after the proposed move has been made
# If the proposed move is invalid, returns the original board instead
def make_move(state, row, col, player):
    if not valid_move(state, row, col, player):
        return state
   
    opposite_player = opposite(player)
    next_state = copy_state(state)
    next_state[row][col] = player
   
    if move_down_valid(state, row, col, player):
        for y in range(row + 1, 8, 1):
            if state[y][col] == opposite_player:
                next_state[y][col] = player
            if state[y][col] == player:
                break

    if move_up_valid(state, row, col, player):
        for y in range(row - 1, -1, -1):
            if state[y][col] == opposite_player:
                next_state[y][col] = player
            if state[y][col] == player:
                break

    if move_left_valid(state, row, col, player):
        for x in range(col - 1, -1, -1):
            if state[row][x] == opposite_player:
                next_state[row][x] = player
            if state[row][x] == player:
                break

    if move_right_valid(state, row, col, player):
        for x in range(col + 1, 8, 1):
            if state[row][x] == opposite_player:
                next_state[row][x] = player
            if state[row][x] == player:
                break

    if move_up_left_valid(state, row, col, player):
        for diff in range(1, 8, 1):
            if row - diff < 0 or col - diff < 0:
                break
            if state[row - diff][col - diff] == opposite_player:
                next_state[row - diff][col - diff] = player
            if state[row - diff][col - diff] == player:
                break

    if move_up_right_valid(state, row, col, player):
        for diff in range(1, 8, 1):
            if row - diff < 0 or col + diff > 7:
                break
            if state[row - diff][col + diff] == opposite_player:
                next_state[row - diff][col + diff] = player
            if state[row - diff][col + diff] == player:
                 break
           
    if move_down_left_valid(state, row, col, player):
        for diff in range(1, 8, 1):
            if row + diff > 7 or col - diff < 0:
                break
            if state[row + diff][col - diff] == opposite_player:
                next_state[row + diff][col - diff] = player
            if state[row + diff][col - diff] == player:
                break

    if move_down_right_valid(state, row, col, player):
        for diff in range(1, 8, 1):
            if row + diff > 7 or col + diff > 7:
                break
            if state[row + diff][col + diff] == opposite_player:
                next_state[row + diff][col + diff] = player
            if state[row + diff][col + diff] == player:
                break

    return next_state


# Provides a random move for a player, assuming a valid move exists
def random_move(state, player):
    valid_moves = list_valid_moves(state, player)
    if valid_moves == []:
        return state
    move = random.choice(valid_moves)
    return move

#######################################################################################


# Your task is to write this function.
# Given the state of the board and your player colour
# Return your move as a list of two coordinates: [row, column]
def my_move(state, player):
    moves_to_avoid = [[0,1],[1,1],[0,1],[6,0],[6,1],[7,1],[0,6],[1,6],[1,7],[6,6],[6,7],[7,6]]
    corners = [[0,0],[0,7],[7,0],[7,7]]
    valid_moves = list_valid_moves(state, player)

    # If no valid moves, do nothing
    if not valid_moves:
        return
   
    # Check if corners are in the valid moves
    for i in corners:
        if i in valid_moves:
            return i
   
    # Check if moves_to_avoid are in valid_moves, then remove them from
    # valid_moves completely, unless there arent any other moves to play
    temp = state
    for i in moves_to_avoid:
        if i in temp:
            valid_moves.pop(valid_moves.index(i))
   
    #maybe make it so that it goes trought the board and picks the first valid move in
    # "valid_move? "unless there is a corner or other favorable move.
 
   
    #(I also just saw a function for a valid move, we could prioratize moves
    # -that would take white peices over?)

    # if we have a corner, try capture adjacent squares
    for coord in corners:
        if coord == player:
            adj_valid = find_adjacent_valid(state, tuple(coord), player)
           
            if adj_valid:
                return random.choice(adj_valid)

   
    for coord in corners:
        valid_coords = find_adj_adj_valid(state, coord, player)
        if valid_coords:
            return random.choice(valid_coords)

    return random_move(state, player)

    # make random move until a corner is captured, then find adjecent
    # squares to that corner, and focus on capturing those


def get_total_moves_played(state):
    count = -4
    for r in state:
        for i in r:
            if i != "_":
                count += 1
    return count

def find_adjacent_valid(state, coords, player):
    x, y = coords
    adj = [[x+1, y], [x, y-1], [x+1,y-1], [x+1,y+1], [x,y+1], [x-1,y-1], [x-1,y], [x-1,y+1]]
    valid = list_valid_moves(state,player)
    if not valid:
        return
    common_coords = common_elements(valid, adj)

    return common_coords

def find_adj_adj_valid(state,coords,player): # coords are gonna be a corner
    x, y = coords
    adj = [[x+1, y], [x, y-1], [x+1,y-1], [x+1,y+1], [x,y+1], [x-1,y-1], [x-1,y], [x-1,y+1]]
    adj_adj = []
    for i in adj:
       adj_adj.append(find_adjacent_valid(state, i, player))
    adj_adj = flatten_2d_array(adj_adj)
    return adj_adj
    # good luck


def flatten_2d_array(arr):
    temp = []
    for i in arr:
        if i == None:
            return
        temp = temp + i
    return temp

def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

       
#######################################################################################

# A little script that runs a game between two bots that choose random moves every time
move_number = 1
state = starting_board()
print("Starting state: ")
print_board(state)
while not game_over(state):
    if has_valid_move(state, "W"):
        move = random_move(state, "W")
        state = make_move(state, move[0], move[1], "W")
        print("White player makes move " + str(move_number) + ":")
        move_number += 1
        print_board(state)
    else:
        print("White player skips their move")

    if game_over(state):
        break
    if has_valid_move(state, "B"):
        move = random_move(state, "B")
        state = make_move(state, move[0], move[1], "B")
        print("Black player makes move " + str(move_number) + ":")
        move_number += 1
        print_board(state)
    else:
        print("Black player skips their move")

scores = count_scores(state)
black_score = scores[0]
white_score = scores[1]
print("Final scores: " + str(black_score) + ":" + str(white_score))
if black_score > white_score:
    print("Black player won")
if white_score > white_score:
    print("White player won")
if black_score == white_score:
    print("It's a TIE!")

