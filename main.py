def draw_board(grid):
    print("-------------")
    for i in range(len(grid)):
        print("|",grid[i],end=" ")
        if (i+1)%3==0:
            print("|")
            print("-------------")
print("Welcome to TicTacToe","\n")
input_grid = [1,2,3,4,5,6,7,8,9]
draw_board(input_grid)

p1 = int(input("P1 select value from 1 to 9: "))
input_grid[p1-1]= "X"
draw_board(input_grid)
p1 = int(input("P1 select value from 1 to 9: "))
input_grid[p1-1]= "X"
draw_board(input_grid)
p1 = int(input("P1 select value from 1 to 9: "))
input_grid[p1-1]= "X"
draw_board(input_grid)

p2 = int(input("P2 select value from 1 to 9: "))
input_grid[p2-1]= "O"
draw_board(input_grid)

def status():
    if input_grid[0:3]==["X","X","X"]or input_grid[3:7]==["X","X","X"] or input_grid[6:]==["X","X","X"]or input_grid[0:7:3]==["X","X","X"] or input_grid[1:8:3]==["X","X","X"] or input_grid[2:9:3]==["X","X","X"] or input_grid[0:9:4]==["X","X","X"]or input_grid[2:7:2]==["X","X","X"]:
        print("Player 1 wins")

    else: 
        print("The match is a draw")

status()

