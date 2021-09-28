""" solution for hackerrank problem cstle on the grid"""
""" kind of silimar to BFS, using similar approach of using queue 
to visit all neighbours accesible in one step (here one step is diffrent
from what happens in bfs)"""

def minimumMoves(grid, startX, startY, goalX, goalY):
    """ calculates and returns minimum number of step, -1 if not accessible"""
    c = 0 #variable for step count
    n = len(grid)  
    visited = set() #set to keep track of visited locations
    visited.add((startX, startY))
    q = deque([[startX, startY, c]])  #queue to track all nodes to be visited, intialise with source cell
    directions = [(1,0),(-1,0),(0,1),(0,-1)]   #single steps in movable dirctions
    
    while q:  #run algorithm while queue is not emply
        x, y, c = q.popleft()  #starting from current leftmost (earliest entered) cell in queue
        c += 1                 #all the neighbours of curr cell will be given count +1 to curr cell
        
        for dirx, diry in directions:
            #for each valid direction, start from current cell
            currx = x
            curry = y
            
            while True:
                #increase cell count in the selcted direction by one step
                currx += dirx
                curry += diry
                if currx < n and curry < n and currx >= 0 and curry >= 0 and grid[currx][curry] == '.':
                    #check for if the cell location is valid, if not then take new direction
                    if currx == goalX and curry == goalY:
                        # if goal cell is reached
                        return c
                    
                    elif (currx, curry) not in visited:
                        # if the cell is not visited and not target, then append it in queue and mark as visited
                        visited.add((currx, curry))
                        q.append([currx, curry, c])
                    
                else:
                    #if the location was not valid, try for next direction
                    break
                        
    return -1 # if target cell is not accessible from source