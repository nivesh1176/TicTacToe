print("Welcome to TicTacToe")
print()

for i in range(3):
    for j in range(3):
        print("|   ", end="") 
    print("|") 
    if i < 2:
        print("----" * 3) 
