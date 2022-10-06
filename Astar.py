from copy import deepcopy

class node:  
  
    def __init__(self, startboard, parent):

        self.board = startboard
        self.parent = parent
        self.fval = 0
        self.gval = 0
        self.hval = 0

    # Misplaced function: checks if the self board and the goal board are equal. 
    # If they are equal, the goal board is found. If they aren't equal, we add one to the counter.
 
    def misplaced(self):
        goal = [[0,1,2],[3,4,5],[6,7,8]]
        inc = 0
        for i in range(3):
            for j in range (3):
                if self.board[i][j] != goal[i][j]:
                    inc += 1
        return inc

    # The manhattan function will check how many moves a number is from its goal position.

    def manhattan(self):
        heuristic_value = 0
        for i in range(3):
            for j in range(3):
                x, y = divmod(self.board[i][j], 3)
                heuristic_value += abs(x-i) + abs(y-j)
        return heuristic_value

# Get the children of the current board function

def find_children(board, x, y):

    board = board.board
        
    children = []

    if x > 0:
        
        newboard = deepcopy(board)
        newboard[x][y]=newboard[x-1][y]
        newboard[x-1][y]=0
        child = node(newboard, board)
        children.append(child)

    
    
    if x < 2:
        newboard = deepcopy(board)
        newboard[x][y]=newboard[x+1][y]
        newboard[x+1][y]=0
        child = node(newboard, board)
        children.append(child)


    if y > 0:
        newboard = deepcopy(board)
        newboard[x][y]=newboard[x][y-1]
        newboard[x][y-1]=0
        child = node(newboard, board)
        children.append(child)

    

    if y < 2:
        newboard = deepcopy(board)
        newboard[x][y]=newboard[x][y+1]
        newboard[x][y+1]=0
        child = node(newboard, board)
        children.append(child)

    return children
       
# A star algorithm with the manhattan heuristic function

def manhattan_Astar(startnode):

    # Initialize an open list and a closed list
    # Define the goal solution of the puzzle

    open_list = []
    closed_list = []
    solution = [[0,1,2], [3,4,5], [6,7,8]]

    # Add the starting node on the open list

    open_list.append(startnode)

    # while the open list is not empty

    while open_list:

        # find the node with the smallest f value on the open list
        
        fval = open_list[0].fval
        index=0
        for i, board in enumerate(open_list):
            if i == 0:
                continue
            if (board.fval < fval):
                fval = board.fval
                index = i
                
        board_smallest_fval, index = open_list[index], index
        
        # checking if the board with the smallest value is equal to the solution
        
        if board_smallest_fval.board == solution:
            return board_smallest_fval

        # We pop the board with the smallest f value off the open list
     
        open_list.pop(index)

        # We generate the children of the board with the smallest f value

        for i in range(3):
            for j in range(3):

                if board_smallest_fval.board[i][j] == 0:
                    x, y = i, j
            
                    break
                
        children = find_children(board_smallest_fval, x, y)


        for child in children:
            in_closed_list = False 

            # checking if a child in children is in closed list  
        
            for i, board in enumerate(closed_list):
                if board.board == child.board:
                    in_closed_list = True
                    break
            
            # if a child in children is not in closed list

            if not in_closed_list: 
                
                present_in_openlist = False

                # checking if a node has the same position as a child is in the open list


                for j, board in enumerate(open_list):
                    if board.board == child.board:
                        present_in_openlist = True

                        # checking if the child has a lower g value than the node in the open list
                        # if the node in the open list has a lower g value than the child then skip this child
                        # if the child has a lower g value than the node then we update the nodes f,g values and we set the parent to the board with the smallest f value


                        if board_smallest_fval.gval + 1  < open_list[j].gval:
                            open_list[j].gval = board_smallest_fval.gval + 1 
                            open_list[j].fval = open_list[j].gval + open_list[j].hval
                            open_list[j].parent = board_smallest_fval

                # if the node with the same position as the child isn't in the open list
                # We update the f,g,h values of the child
                # We set the parent of the child to the board with the smallest f value
                # We add the child node to the open list


                if not present_in_openlist:

                    child.gval = board_smallest_fval.gval + 1 
                    child.hval = child.manhattan()
                    child.fval = child.gval + child.hval
                    child.parent = board_smallest_fval
                    open_list.append(child)

        # We append the board with the smallest f value to the closed list

        closed_list.append(board_smallest_fval)

    return None

# A star algorithm for the misplaced heuristic function

def misplaced_Astar(startnode): 

    # Initialize an open list and a closed list
    # Define the goal solution of the puzzle

    open_list = []
    closed_list = []
    solution = [[0,1,2],[3,4,5],[6,7,8]]

    # Add the starting node on the open list

    open_list.append(startnode)

    # while the open list is not empty

    while open_list:
        
        # find the node with the smallest f value on the open list

        fval = open_list[0].fval
        index=0
        for i, board in enumerate(open_list):
            if i == 0:
                continue
            if (board.fval < fval):
                fval = board.fval
                index = i
                
        board_smallest_fval, index = open_list[index], index

        # checking if the board with the smallest value is equal to the solution
        
        if board_smallest_fval.board == solution:
            return board_smallest_fval
        
        # We pop the board with the smallest f value off the open list

        open_list.pop(index)

        # We generate the children of the board with the smallest f value
        
        for i in range(3):
            for j in range(3):
            
                if board_smallest_fval.board[i][j] == 0:
                    x, y = i, j
        
                    break

        children = find_children(board_smallest_fval, x, y)

        for child in children:
            
            in_closed_list = False   

             # checking if a child in children is in closed list
            
        
            for i, board in enumerate(closed_list):
                if board.board == child.board:
                    in_closed_list = True
                    break

            # if a child in children is not in closed list
            

            if not in_closed_list: 

                present_in_openlist = False

                # checking if a node has the same position as a child is in the open list


                for j, board in enumerate(open_list):
                    if board.board == child.board:
                        present_in_openlist = True

                        # checking if the child has a lower g value than the node in the open list
                        # if the node in the open list has a lower g value than the child then skip this child
                        # if the child has a lower g value than the node then we update the nodes f,g values and we set the parent to the board with the smallest f value

                        if board_smallest_fval.gval + 1  < open_list[j].gval:
                            open_list[j].gval = board_smallest_fval.gval + 1 
                            open_list[j].fval = open_list[j].gval + open_list[j].hval
                            open_list[j].parent = board_smallest_fval

                # if the node with the same position as the child isn't in the open list
                # We update the f,g,h values of the child
                # We set the parent of the child to the board with the smallest f value
                # We add the child node to the open list

                if not present_in_openlist:

                    child.gval = board_smallest_fval.gval + 1 
                    child.hval = child.misplaced()
                    child.fval = child.gval + child.hval
                    child.parent = board_smallest_fval
                    open_list.append(child)

        # We append the board with the smallest f value to the closed list

        closed_list.append(board_smallest_fval)            

            
    return None

# create matrix function

def make_matrix():
    for i in boards_solution:
        for j in i:
            print(j)
        print()
        
# main run

if __name__ == "__main__":


# passing user input as a list of integers

    a = input("Enter 8 numbers all different from each other between 0-8 (make sure there is a space between each number) : ")
    user_list = a.split()


    # Converting each item to int type

    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])

    # getting the first three elements of the list and putting them a separate list

    firstpart = user_list[0:3]
    secondpart = user_list[3:6]
    thirdpart = user_list[6:9]

    # make new list

    startboardlist=[]

    # append the three lists to the new list

    startboardlist.append(firstpart)
    startboardlist.append(secondpart)
    startboardlist.append(thirdpart)


    # define start puzzle

    start = node(startboardlist,None)

    # User input 

    boards_solution = []


    b = input("Choose 0 for Manhattan or 1 for Misplaced : ")

    # solve with manhattan heuristic function

    if b == "0":
        goal = manhattan_Astar(start)
        boards_solution.append(start.board)
        if (not goal):
            print ("No solution for this 8 puzzle")
        else:
            boards_solution.append(goal.board)
            parents=goal.parent
            while parents:
                boards_solution.append(parents.board)
                parents = parents.parent
        make_matrix()
        print("length = ", (len(boards_solution)-2))
        print()
        
        
    # solve with misplaced heuristic function

    else:       
        goal = misplaced_Astar(start)
        boards_solution.append(start.board)
        if (not goal):
            print ("No solution for this 8 puzzle")
        else:
            boards_solution.append(goal.board)
            parents=goal.parent
            while parents:
                boards_solution.append(parents.board)
                parents = parents.parent
        make_matrix()
        print("length = ", (len(boards_solution)-2))
        print()
