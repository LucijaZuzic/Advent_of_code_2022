import numpy as np
import os

path = ""


def parse_block(block,delimiters = None,type_lookup = None, allInt = False, allFloat = False):
    list_out = []

    pattern = None
    if delimiters is not None and len(delimiters)>0:
        if type(delimiters) is str:
            pattern = r'|'.join([delimiters])

        elif type(delimiters) is list:
            pattern = r'|'.join(delimiters)

    for line in block:
        temp = line.strip('\n')
        if delimiters is None or len(delimiters)==0:
            list_out.append(temp)
        else:
            new_item = []
            split_list = split(pattern, temp)

            for string in split_list:
                if string != '':
                    new_item.append(string)

            for i in range(len(new_item)):
                if allInt:
                    new_item[i] = int(new_item[i])
                elif allFloat:
                    new_item[i] = float(new_item[i])
                elif type_lookup is not None:
                    if type(type_lookup) is list:
                        if type_lookup[i]=='int':
                            new_item[i] = int(new_item[i])
                        elif type_lookup[i]=='float':
                            new_item[i] = float(new_item[i])
                    elif type(type_lookup) is dict:
                        if i in type_lookup:
                            if type_lookup[i]=='int':
                                new_item[i] = int(new_item[i])
                            elif type_lookup[i]=='float':
                                new_item[i] = float(new_item[i])
            list_out.append(new_item)

    return list_out

#parses a file that is just a single column of items that are sometimes separated by empty lines
#returns as a list of lists where the outer list corresponds to a list of blocks 
#where each block is separated by an empty line
#and the inner list corresponds to a list of each item in a given block
def parse_split_by_emptylines(path,fname,delimiters = None,type_lookup = None, allInt = False, allFloat = False):
    load_name = os.path.join(path,fname)

    list_out = []
    with open(load_name) as f:
        new_item = []
        for line in f.readlines():
            temp = line.strip('\n')

            if temp == '' and len(new_item)>0:
                list_out.append(parse_block(new_item,delimiters,type_lookup, allInt, allFloat))
                new_item = []

            elif temp!= '':
                new_item.append(temp)

        if len(new_item)>0:
            list_out.append(parse_block(new_item,delimiters,type_lookup, allInt, allFloat))

        return list_out
    return None

def parse_input01(fname):
    data = parse_split_by_emptylines(path,fname,delimiters = [],type_lookup = None, allInt = False, allFloat = False)

    board = data[0]
    instructions = data[1][0]

    height = len(board)
    width = 0

    for i in range(height):
        board[i]=list(board[i])
        width = max(width,len(board[i]))

    for i in range(height):
        board[i]=board[i]+[' ']*(width-len(board[i]))

    instructions = instructions.replace('R',' R ')
    instructions = instructions.replace('L',' L ')
    instructions = instructions.split(' ')

    command_list = []

    for item in instructions:
        if item!='':
            command_list.append(item)

    return board, command_list

#directions are coded as integers 0: Right, 1: Down 2: Left, 3: Up

#maps directions to vector representation
direction_dict = {0:np.array([0,1]),1:np.array([1,0]),2:np.array([0,-1]),3:np.array([-1,0])}

#maps left/right commands to corresponding increment in direction
rotation_dict = {'L':-1,'R':1}

#maps directions to corresponding symbols when printing on grid
direction_character_dict = {0:'>',1:'v',2:'<',3:'^'}

#diagonals are coded as 0: Down-Right, 1: Down-Left, 2: Up-Left, 3: Up-Right

#maps diagonals to corresponding vectors
diagonal_dict = {0:np.array([1,1]),1:np.array([1,-1]),2:np.array([-1,-1]),3:np.array([-1,1])}


#returns True if a grid coordinate is out of bounds of the grid we've been provided
def on_exterior(coords,board):
    return coords[0]<0 or coords[1]<0 or coords[0]>=len(board) or coords[1]>=len(board[0]) or board[coords[0]][coords[1]]==' '

#returns True if a grid coordinate is in-bounds for the grid we've been provided
def on_interior(coords,board):
    return not on_exterior(coords,board)

#move one step along grid
def execute_step(coords,direction,board,adjacency_dict):
    #compute nominal coordinates/direction after executing step
    next_coords = coords+direction_dict[direction]
    next_direction = direction

    #move the naive motion would take us out of bounds of the map
    if on_exterior(next_coords,board):

        #use the adjacency matrix to find where on the map (and in what direction)
        #we would actually end up
        key_in = (tuple(coords.tolist()),direction)

        next_coords = np.array(list(adjacency_dict[key_in][0]))
        next_direction = adjacency_dict[key_in][1]

    #if the next location would cause us to run into a wall, do nothing
    if board[next_coords[0]][next_coords[1]]=='#':
        return coords, direction

    #otherwise, return updated coordinates/direction
    else:
        return next_coords, next_direction

#run a single command in the path that the monkeys gave us
def execute_command(coords,direction,command,board,boundary_dict):
    #update the grid for visualizaton purposes (showing our path)
    board[coords[0]][coords[1]]=direction_character_dict[direction]

    #if given a rotation command
    if command=='L' or command=='R':
        #update the direction accordingly
        direction+=rotation_dict[command]
        direction%=4
    #if given a forward motion command
    else:
        #move forward by the number of steps that have been commanded

        num_steps = int(command)

        for i in range(num_steps):
            #update the grid for visualizaton purposes (showing our path)
            board[coords[0]][coords[1]]=direction_character_dict[direction]

            #move forward a single step
            coords, direction = execute_step(coords,direction,board,boundary_dict)

    return coords,direction

#execute a single step when traveling along the perimeter of the map
#note that it makes the assumption that we are starting from an "inner corner" of the 2D pattern
#then moving outwards, and this perimeter traversal will terminate before we hit another inner corner
#As such, the only corners that will be "rounded" are outer corners, meaning that moving along the tangential
#direction would bring us into the exterior of the pattern (not the case for inner corners)
#note that, as with the rest of this algorithm, things will break if any dimension of the cube has length 1!
def perimeter_step(coords,direction,board):
    #compute the nominal next grid coordinates after moving forward along the perimeter 1 step
    next_coords = coords+direction_dict[direction]

    #if moving in the current direction would take us to the exterior of the 2D pattern
    if on_exterior(next_coords,board):
        #computer the directions that are left/right of the current one
        #as well as the adjacent grid points in these two directions

        directionL = (direction-1)%4
        next_coordsL = coords+direction_dict[directionL]

        directionR = (direction+1)%4
        next_coordsR = coords+direction_dict[directionR]

        #whichever of these directions would keep us on the interior of the map is the new direction
        #since we are rounding a corner, we keep the current coordinates, and just change the direction
        if on_interior(next_coordsL,board):
            return coords, directionL

        if on_interior(next_coordsR,board):
            return coords, directionR

    return next_coords, direction

#checks for grid-points in the 2D pattern that are "inner corners"
#these correspond to locations where a zipper starts on the cube
#grid points who have all four north/east/south/west neighbors, but are missing 1 diagonal neighbor
#are considered to the locations of inner corners. 
#the location of the missing diagonal neighbor tells us which two cardinal directions to travel in
#to leave th inner corner and travel along the perimeter
#note that, as with the rest of this algorithm, things will break if any dimension of the cube has length 1!
def check_if_inner_corner(coords,board):
    if on_exterior(coords,board):
        return False, None

    diag_list = []

    for i in range(4):
        if on_exterior(coords+diagonal_dict[i],board):
            diag_list.append(i)

    dir_list = []
    for i in range(4):
        if on_exterior(coords+direction_dict[i],board):
            dir_list.append(i)

    if len(diag_list)!=1 or len(dir_list)!=0:
        return False, None

    d0 = diag_list[0]
    d1 = (diag_list[0]+1)%4

    return True, [d0,d1]

#starting from an inner corner, zip up the cube, generating the corresponding 
#adjacency mapping of (coord,direction)<->(coord,direction) for seams of the cube
#we'll need to do this for several inner corners to get the complete map
def zip_up_edges_from_corner(coords,direction_pair,board,dict_in):
    direction0 = direction_pair[0]
    direction1 = direction_pair[1]

    direction0_prev = direction0
    direction1_prev = direction1

    coords0 = coords+direction_dict[direction0]
    coords1 = coords+direction_dict[direction1]

    #travel along the perimeter of the 2D pattern in opposite directions
    #this process continues until 2 corners are rounded simultaneously during the traversal
    while direction0 == direction0_prev or direction1_prev == direction1:
        direction0_prev = direction0
        direction1_prev = direction1

        #identify the inner/outer normal directions for both line segments we are currently looking at
        normal_direction_outer0 = (direction0+1)%4
        if on_interior(coords0+direction_dict[normal_direction_outer0],board):
            normal_direction_outer0 = (direction0-1)%4

        normal_direction_outer1 = (direction1+1)%4
        if on_interior(coords1+direction_dict[normal_direction_outer1],board):
            normal_direction_outer1 = (direction1-1)%4

        normal_direction_inner0 = (normal_direction_outer0+2)%4
        normal_direction_inner1 = (normal_direction_outer1+2)%4

        #update the adjacency map using current coords and inner/outer normals
        dict_in[(tuple(coords0.tolist()),normal_direction_outer0)]=(tuple(coords1.tolist()),normal_direction_inner1)
        dict_in[(tuple(coords1.tolist()),normal_direction_outer1)]=(tuple(coords0.tolist()),normal_direction_inner0)

        #move along the perimeter in each direction by one step
        coords0, direction0 = perimeter_step(coords0,direction0,board)
        coords1, direction1 = perimeter_step(coords1,direction1,board)

#zip up the entire cube
def generate_off_grid_adjacency_cube(board):
    dict_out = {}

    #check every grid point
    for i in range(len(board)):
        for j in range(len(board[0])):
            coords = np.array([i,j])

            #if the grid point is an inner corner,
            #perform a single zip starting from that grid point
            corner_bool, direction_pair = check_if_inner_corner(coords,board)
            if corner_bool:
                zip_up_edges_from_corner(coords,direction_pair,board,dict_out)

    return dict_out

#this is for part 1: construct the adjacency map using the wrap-rule
def generate_off_grid_adjacency_wrap(board):
    dict_out = {}

    for i in range(len(board)):
        left = 0
        while board[i][left]==' ':
            left+=1


        right = len(board[0])-1
        while board[i][right]==' ':
            right-=1

        dict_out[((i,left),2)]=((i,right),2)
        dict_out[((i,right),0)]=((i,left),0)

    for i in range(len(board[0])):
        top = 0
        while board[top][i]==' ':
            top+=1

        bottom = len(board)-1
        while board[bottom][i]==' ':
            bottom-=1

        dict_out[((top,i),3)]=((bottom,i),3)
        dict_out[((bottom,i),1)]=((top,i),1)

    return dict_out


#only difference between solution01/solution02 is the
#adjacency map used for gridpoints that are out of bounds

#runs part 1
def solution01(): 
    fname = 'input_day22.txt'

    board, command_list = parse_input01(fname)

    adjacency_dict = generate_off_grid_adjacency_wrap(board)

    coords = np.array([0,0])
    while board[coords[0]][coords[1]]==' ':
        coords[1]+=1
    
    direction = 0

    for command in command_list:
        coords,direction = execute_command(coords,direction,command,board,adjacency_dict)

    code = 1000*(coords[0]+1)+4*(coords[1]+1)+direction
    print(code)

#runs part 2
def solution02(): 
    fname = 'input_day22.txt'

    board, command_list = parse_input01(fname)

    adjacency_dict = generate_off_grid_adjacency_cube(board)

    coords = np.array([0,0])
    while board[coords[0]][coords[1]]==' ':
        coords[1]+=1

    direction = 0

    for command in command_list:
        coords,direction = execute_command(coords,direction,command,board,adjacency_dict)

    code = 1000*(coords[0]+1)+4*(coords[1]+1)+direction
    print(code)



if __name__ == '__main__': 
    solution01()
    solution02() 