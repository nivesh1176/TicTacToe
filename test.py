def draw_board(grid):
    print("-------------")
    for i in range(len(grid)):
        print("|",grid[i],end=" ")
        if (i+1)%3==0:
            print("|")
            print("-------------")
def status(): # error here printing both values.
    if input_grid[0:3]==["X","X","X"]or input_grid[3:6]==["X","X","X"] or input_grid[6:]==["X","X","X"]or input_grid[0:7:3]==["X","X","X"] or input_grid[1:8:3]==["X","X","X"] or input_grid[2:9:3]==["X","X","X"] or input_grid[0:9:4]==["X","X","X"]or input_grid[2:7:2]==["X","X","X"]:
        print("Player 1 wins")
    if input_grid[0:3]==["O","O","O"]or input_grid[3:6]==["O","O","O"] or input_grid[6:]==["O","O","O"]or input_grid[0:7:3]==["O","O","O"] or input_grid[1:8:3]==["O","O","O"] or input_grid[2:9:3]==["O","O","O"] or input_grid[0:9:4]==["O","O","O"]or input_grid[2:7:2]==["O","O","O"]:
        print("Player 2 wins")
    elif input_grid[0:3] != ["X", "X", "X"] or input_grid[3:6] != ["X", "X", "X"] or input_grid[6:] != ["X", "X", "X"] or input_grid[0:7:3] != ["X", "X", "X"] or input_grid[1:8:3] != ["X", "X", "X"] or input_grid[2:9:3] != ["X", "X", "X"] or input_grid[0:9:4] != ["X", "X", "X"] or input_grid[2:7:2] != ["X", "X", "X"] or input_grid[0:3] != ["O", "O", "O"] or input_grid[3:6] != ["O", "O", "O"] or input_grid[6:] != ["O", "O", "O"] or input_grid[0:7:3] != ["O", "O", "O"] or input_grid[1:8:3] != ["O", "O", "O"] or input_grid[2:9:3] != ["O", "O", "O"] or input_grid[0:9:4] != ["O", "O", "O"] or input_grid[2:7:2] != ["O", "O", "O"]:
        print("The Match is Draw")

print("Welcome to TicTacToe","\n")
input_grid = [1,2,3,4,5,6,7,8,9]
draw_board(input_grid)
# made input functions
def input_1():
    while True:
        p1 = input("P1 select value from 1 to 9: ")
        if p1.isdigit():
            p1 = int(p1)
            if 1 <= p1 <= 9:
                input_grid[p1-1]= "X"
                draw_board(input_grid)
                return
            else:
                print("Enter a valid value between 1 and 9")
                
        else:
            print("Enter a valid value between 1 and 9")
        
def input_2():
    while True:
        p2 = input("P2 select value from 1 to 9: ")
        if p2.isdigit():
            p2 = int(p2)
            if 1 <= p2 <= 9:
                input_grid[p2-1]= "O"
                draw_board(input_grid)
                return
            else:
                print("Enter a valid value between 1 and 9")
                input_2()
        else:
            print("Enter a valid value between 1 and 9")
            input_2()
def main_input():
    for j in range(9):
        if j%2==0:
            input_1()
        else :
            input_2()
 
main_input()
status()
