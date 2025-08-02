import pygame

def solve_maze(maze, pos) -> list:

    curr_cell = pos
    queque = [curr_cell]                    # store cell order - contains tuple (col,row)
    visited = [curr_cell]                   # to store visited cells
    steps = [(0,1), (0,-1), (1,0), (-1,0)]  # define possible steps
    goal = (len(maze)-2, len(maze)-2)

    while True:
        found_one = False
        for step in steps:
            neighbor = (curr_cell[0] + step[0], curr_cell[1] + step[1])
            if maze[neighbor[1]][neighbor[0]] == 0 and neighbor not in visited:
                curr_cell = neighbor        # update curr_cell              
                queque.append(neighbor)     # store coords
                visited.append(neighbor)    # mark cell as visited
                found_one = True            # cell is no dead end
                break                       # leave for loop
        if not found_one: 
            try:
                # remove dead end cell from queque          
                queque.pop(-1)
                # return to cell before - not working if player is at treasure
                curr_cell = queque[-1]      
            except:
                break
            
        elif curr_cell == goal:
            break   # end search

    return queque
