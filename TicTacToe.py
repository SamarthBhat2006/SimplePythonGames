board = [""]*9

def show():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def win(p):
    return((board[0]== board[1] == board[2] == p) or
           (board[3]== board[4] == board[5] == p) or
           (board[6]== board[7] == board[8] == p) or
           (board[0]== board[3] == board[6] == p) or
           (board[1]== board[4] == board[7] == p) or
           (board[2]== board[5] == board[8] == p) or
           (board[0]== board[4] == board[8] == p) or
           (board[2]== board[4] == board[6] == p))
player = "X"
moves = 9
while moves > 0:
    show()
    move = int(input("Player " + player + ", enter your move (1-9): "))-1
    if move < 0 or move > 8 or board[move] != "":
        print("Invalid move. Try again.")
        continue
    if board[move] == "":
        board[move] = player
        moves -= 1
    else:
        print("That space is already taken. Try again.")
        continue
    if win(player):
        show()
        print("Player " + player + " wins!")
        
        break
    player = "O" if player == "X" else "X"    
    if moves == 0:   
        show()
        print("It's a tie!")