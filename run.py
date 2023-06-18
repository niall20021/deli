import random

# Board dimensions
BOARD_SIZE = 8

# Ship configurations
SHIP_LENGTHS = [2, 3, 4]
NUM_SHIPS = len(SHIP_LENGTHS)

# Function to initialize the game board
def initialize_board():
    board = []
    for _ in range(BOARD_SIZE):
        row = []
        for _ in range(BOARD_SIZE):
            row.append('O')
        board.append(row)
    return board

# Function to randomly place ships on the board
def place_ships(board):
    ships = []
    for length in SHIP_LENGTHS:
        ship = []
        while True:
            x = random.randint(0, BOARD_SIZE - 1)
            y = random.randint(0, BOARD_SIZE - 1)
            orientation = random.choice(['horizontal', 'vertical'])
            positions = []

            if orientation == 'horizontal':
                if y + length <= BOARD_SIZE:
                    positions = [(x, y+i) for i in range(length)]
            else:
                if x + length <= BOARD_SIZE:
                    positions = [(x+i, y) for i in range(length)]

            if positions and all(board[x][y] == 'O' for x, y in positions):
                ship = positions
                break
        
        for x, y in positions:
            board[x][y] = 'S'
        ships.append(ship)
    return ships

# Function to print the board
def print_board(board):
    print('   ' + ' '.join([str(i) for i in range(BOARD_SIZE)]))
    print('  ' + '-' * (BOARD_SIZE * 2 + 1))
    for i in range(BOARD_SIZE):
        print(str(i) + ' | ' + ' '.join(board[i]))

# Function to check if all ships have been sunk
def check_game_over(ships):
    for ship in ships:
        if ship:
            return False
    return True

# Main game loop
def play_battleship():
    board = initialize_board()
    ships = place_ships(board)

    print("Welcome to Battleship!")
    print("Sink all the ships to win the game.")

    while True:
        print("\n====================================")
        print_board(board)
        print("Take a shot!")
        x = input("Enter the X coordinate (0-7):\n")
        y = input("Enter the Y coordinate (0-7):\n")

        if not x.isdigit() or not y.isdigit():
            print("Error: Invalid coordinates. Please enter numeric values.")
            continue

        x = int(x)
        y = int(y)

        if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
            print("Error: Invalid coordinates. Please enter values within the board range (0-8).")
            continue

        if board[x][y] == 'S':
            print("Hit!")
            board[x][y] = 'X'
            for ship in ships:
                if (x, y) in ship:
                    ship.remove((x, y))
                    if not ship:
                        ships.remove(ship)
                        print("You sunk a ship!")
                        if check_game_over(ships):
                            print("Congratulations! You won!")
                            return
        elif board[x][y] == 'X':
            print("You've already hit that spot!")
        else:
            print("Miss!")
            board[x][y] = 'M'

# Start the game
play_battleship()
