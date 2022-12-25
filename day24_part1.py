file = open("input_day24.txt", "r")
lines = file.readlines()    
blizzards = set() 
occupied = dict()
width = 0
height = len(lines) - 2
myx = 1
myy = 0
for i in range(len(lines)):
    width = len(lines[i]) - 2
    lines[i] = lines[i].replace("\n", "")
    for j in range(len(lines[i])):
        if lines[i][j] == '>':
            blizzards.add((len(blizzards), j, i, 0))
            if (j, i) in occupied:
                occupied[(j, i)] += 1
            else:
                occupied[(j, i)] = 1
        if lines[i][j] == '<':
            blizzards.add((len(blizzards), j, i, 1))
            if (j, i) in occupied:
                occupied[(j, i)] += 1
            else:
                occupied[(j, i)] = 1
        if lines[i][j] == '^':
            blizzards.add((len(blizzards), j, i, 2))
            if (j, i) in occupied:
                occupied[(j, i)] += 1
            else:
                occupied[(j, i)] = 1
        if lines[i][j] == 'v':
            blizzards.add((len(blizzards), j, i, 3))
            if (j, i) in occupied:
                occupied[(j, i)] += 1
            else:
                occupied[(j, i)] = 1

possible_positions = dict()
front = set()
front.add((myx, myy))

def printBlizzards():
    for j in range(1, height + 1):
        strpr = ""
        for i in range(1, width + 1):
            if (i, j) in front:
                strpr += 'E'
                continue
            if (i, j) in occupied and occupied[(i, j)] > 0:
                strpr += str(occupied[(i, j)])
                continue    
            strpr += '.'
        print(strpr) 
  
found = False
minmoves = 0
for move in range(300):
    new_blizzards = set()
    new_occupied = dict()
    for blizzard in blizzards:
        id = blizzard[0]
        x = blizzard[1]
        y = blizzard[2]
        dir = blizzard[3]
        if dir == 0:
            x += 1
            if x > width:
                x = 1
        if dir == 1:
            x -= 1
            if x < 1:
                x = width
        if dir == 2:
            y -= 1
            if y < 1:
                y = height
        if dir == 3:
            y += 1
            if y > height:
                y = 1
        new_blizzards.add((id, x, y, dir))
        if (x, y) in new_occupied:
            new_occupied[(x, y)] += 1
        else:
            new_occupied[(x, y)] = 1 
    blizzards = new_blizzards
    occupied = new_occupied
    new_front = set()
    for f in front:
        tx = f[0]
        ty = f[1]
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                if dx != 0 and dy != 0:
                    continue  
                nx = tx + dx
                ny = ty + dy
                if nx < 1 or nx > width:
                    continue
                if ny < 1 or ny > height:
                    if not (nx == 1 and ny == 0) and not (nx == width and ny == height + 1):
                        continue 
                if (nx, ny) in occupied and occupied[(nx, ny)] > 0: 
                    continue
                if (nx, ny) not in possible_positions:
                    possible_positions[(nx, ny)] = move
                    if nx == width and ny == height:
                        found = True
                        minmoves = move
                        break 
                new_front.add((nx, ny))
            if found:
                break
        if found:
            break
    if found:
        break
    front = new_front 
print(move + 2)