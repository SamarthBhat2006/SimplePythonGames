piles = [3, 4, 5]   # number of sticks in each pile
player = 1

while sum(piles) > 0:

    print("\nPiles:", piles)
    print("Player", player)

    pile = int(input("Choose pile (1, 2, or 3): ")) - 1
    sticks = int(input("How many sticks to remove: "))

    if pile < 0 or pile > 2 or sticks <= 0 or sticks > piles[pile]:
        print("Invalid move. Try again.")
        continue

    piles[pile] = piles[pile] - sticks

    # change player
    if player == 1:
        player = 2
    else:
        player = 1

# last player who played wins
if player == 1:
    print("\nPlayer 2 wins!")
else:
    print("\nPlayer 1 wins!")