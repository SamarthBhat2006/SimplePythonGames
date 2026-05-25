def is_safe(board, row, col, n):
    for i in range(row):
        # Check column conflict
        if board[i] == col:
            return False
        # Check diagonal conflict (row difference == column difference)
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n):
    if row == n:
        print_solution(board, n)
        print()
        return
        
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n)
            # Backtrack implicitly happens here when control returns

def print_solution(board, n):
    print("Solution:")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(". ", end="")
        print()

n = int(input("Enter the No of queens: "))
board = [-1] * n
solve(board, 0, n)