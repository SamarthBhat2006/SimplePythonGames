stones = 10
player = 1
while stones > 0:
    print("There are " + str(stones) + " stones left.")
    move = int(input("Player " + str(player) + ", how many stones do you want to take (1-3)? "))
    if move < 1 or move > 3:
        print("Invalid move. Try again.")
        continue
    if move > stones:
        print("Not enough stones left. Try again.")
        continue
    stones -= move
    if stones == 0:
        print("Player " + str(player) + " wins!")
        break
    player = 2 if player == 1 else 1