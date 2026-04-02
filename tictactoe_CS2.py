def print_board(board):
    '''
    creates board and prints it will current state of board
    args:
        board:(str) board structure
    return:
        prints board of current state
    '''
    print(f'''
   1   2   3
 1 {board[0][0]} | {board[0][1]} | {board[0][2]}
   ---------
 2 {board[1][0]} | {board[1][1]} | {board[1][2]}
   ---------
 3 {board[2][0]} | {board[2][1]} | {board[2][2]}
      ''')

def make_move(board, player):
    '''
    Asks the player for a valid row and column
    args: 
        board: (str) prints board 
        player: (int) player 
    return:
        return board with marked spot that player chose
    '''
    while True:    
        row = int(input(f'Player {player}, enter a row: ')) - 1
        col = int(input(f'Player {player}, enter a column: ')) - 1

        if board[row][col] != ' ':
            print("Spot is already taken")
            continue
        board[row][col] = player
        break 


def check_winner(board):
    '''
    Checks all winning combonations. 
    args:
        board:(str) board structure
    return: 
        return true if there is a winning combo; win = True
    '''
    winning_combos = [[board[1][0], board[1][1], board[1][2]], [board[2][0], board[2][1], board[2][2]], [board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]], [board[0][0], board[0][1], board[0][2]], [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    win = False

    for combo in winning_combos:
        if combo[0] == ' ':
            continue
        if combo[0] == combo[1] and combo[0] == combo[2]:
            win = True                
    return win
    #for every winning combo:
        #if everything in that combo list is the same but not a space OR if it's equal to x or o
            #return True



def main():
    while True:
        player_1 = input("Player 1 would you like to be X or O? ").upper()

        if player_1 not in ['X','O']:
            continue
        if player_1 == 'X':
            player_2 = 'O'
        else:
            player_2 = 'X'
        break

    board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    
    print_board(board)
    board_counter = 0

    while True:
        make_move(board, player_1)
        print_board(board)
        check_winner(board)
        board_counter += 1
        
        if check_winner(board):
            print("Player 1 wins!")
            break
        if board_counter == 9:
            print("Its a tie!")
            break

        make_move(board, player_2)
        print_board(board)
        check_winner(board)
        board_counter += 1

        if check_winner(board):
            print("Player 2 wins!")
            break
        

main()


