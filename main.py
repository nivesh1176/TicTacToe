print("Welcome to TicTacToe")
print()
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    print(" | ".join(map(str, row)))
    print("-" * 9)
