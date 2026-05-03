import random
def print_board(board):
     print(f'''
    1    2    3    4    5 
 1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
   -----------------------
 2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}
   -----------------------
 3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}
   -----------------------
 4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} 
   -----------------------
 5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}
      ''')
     

def place_ships(board, bot_or_player):
    ships = []
    i = 0

    print_board(board)

    while i < 4:
        if bot_or_player == 'p':
            row = int(input(f'Enter a row to place your ship: ')) - 1

            if row < 0 or row >= 5:
                print("number must be 1-5")
                continue

            col = int(input(f'Enter a column to place your ship: ')) - 1

            if col < 0 or col >= 5:
                print("number must be 1-5") 
                continue
        else:
            row = random.randint(0, 4)
            col = random.randint(0, 4)

        if board[row][col] == '🚢':
            continue
        i += 1
        board[row][col] = '🚢'
        ships.append((row, col))

        if bot_or_player == 'p':
            print_board(board)
    return ships

def make_shot(display_board, board, bot_or_player, shots):
    shots = []

    while True:
        if bot_or_player == 'p':
            row = int(input(f'Shoot! Enter a row: ')) - 1

            if row < 0 or row > 4:
                print("number must be 1-5")
                continue

            col = int(input(f'Shoot! Enter a column: ')) - 1  

            if col < 0 or col > 4:
                print("number must be 1-5") 
                continue
        else:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        
        if display_board[row][col] != '⚓':
            continue
        break
        
    if board[row][col] == '🚢':
        display_board[row][col] = '💥'
    
    else:
        display_board[row][col] = '😢'
    
    shots.append((row, col))
    print_board(display_board)


def check_winner(shots, ships):
    for ship in ships:
        if ship not in shots:
            return False
    return True


def main():
    p_board = [['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5]
    b_board = [['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5]
    p_display_board = [['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5]
    b_display_board = [['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5, ['⚓']*5]

    p_shots = []
    b_shots = []
    p_ships = place_ships(p_board, 'p')
    b_ships = place_ships(b_board, 'b')

    while True:
        print_board(b_display_board)
        make_shot(b_display_board, b_board, 'p', p_shots) 
        print_board(b_display_board)

        if check_winner(p_shots, b_ships):
            print('Player wins')
            break

        print_board(p_display_board)
        make_shot(p_display_board, p_board, 'b', b_shots) 
        print_board(p_display_board)

        if check_winner(b_shots, p_ships):
            print('Bot wins')
            break

main()