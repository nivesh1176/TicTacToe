def board():
    print("-------------")
    for i in range(len(grid)):
        print("|",grid[i],end=" ")
        if (i+1)%3==0:
            print("|")
            print("-------------")
print("Welcome to TicTacToe","\n")
grid = [1,2,3,4,5,6,7,8,9]
board()