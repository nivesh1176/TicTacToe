def status(input_grid):
    if input_grid[0:3]==["X","X","X"]or input_grid[3:6]==["X","X","X"] or input_grid[6:]==["X","X","X"]or input_grid[0:7:3]==["X","X","X"] or input_grid[1:8:3]==["X","X","X"] or input_grid[2:9:3]==["X","X","X"] or input_grid[0:9:4]==["X","X","X"]or input_grid[2:7:2]==["X","X","X"]:
        print("Player 1 wins")
    if input_grid[0:3]==["O","O","O"]or input_grid[3:6]==["O","O","O"] or input_grid[6:]==["O","O","O"]or input_grid[0:7:3]==["O","O","O"] or input_grid[1:8:3]==["O","O","O"] or input_grid[2:9:3]==["O","O","O"] or input_grid[0:9:4]==["O","O","O"]or input_grid[2:7:2]==["O","O","O"]:
        print("Player 2 wins")
    else: 
        for i in range(9):
            if i<9:
                continue
            else:
                print("The match is a draw")

# grid=[1,2,3,4,5,6,7,8,9]
# grid=['X','X',3,4,5,6,7,8,9]
# grid=['X','X','X','X','X','X','X','X','X']
status(grid)
