file = open("input_day9.txt", "r") 
lines = file.readlines()
positions = [(0, 0) for i in range(10)]
set_of_pos = [set() for i in range(10)]
set_9_pos = set()
def move_knot(index, dir, step):
    hx = positions[index][0]
    hy = positions[index][1]
    tx = positions[index + 1][0]
    ty = positions[index + 1][1]
    if dir == 'R':
        hx += step
    if dir == 'L':
        hx -= step
    if dir == 'U':
        hy += step
    if dir == 'D':
        hy -= step
    deltax = abs(hx - tx)
    deltay = abs(hy - ty)
    oldtx = tx
    oldty = ty 
    if deltay > deltax:
        if hy > ty:
            dir = 'U'
        else:
            if hy < ty:
                dir = 'D'
    else:
        if deltay < deltax:
            if hx > tx:
                dir = 'R'
            else:
                if hx < tx:
                    dir = 'L'
        else:
            dir = 'S'
    if deltax > 1 or deltay > 1:
        if hx == tx:
            if ty < hy:
                for i in range(ty, hy): 
                    set_of_pos[index + 1].add((tx, i)) 
                ty = hy - 1 
            if ty > hy:
                for i in range(ty, hy, -1): 
                    set_of_pos[index + 1].add((tx, i)) 
                ty = hy + 1 
        else:
            if hy == ty:
                if tx < hx:
                    for i in range(tx, hx): 
                        set_of_pos[index + 1].add((i, ty)) 
                    tx = hx - 1 
                if tx > hx:
                    for i in range(tx, hx, -1): 
                        set_of_pos[index + 1].add((i, ty)) 
                    tx = hx + 1 
            else:
                if dir == 'R':
                    for i in range(tx + 1, hx): 
                        set_of_pos[index + 1].add((i, hy)) 
                    tx = hx - 1
                    ty = hy
                if dir == 'L':
                    for i in range(tx - 1, hx, -1): 
                        set_of_pos[index + 1].add((i, hy)) 
                    tx = hx + 1
                    ty = hy
                if dir == 'U':
                    for i in range(ty + 1, hy): 
                        set_of_pos[index + 1].add((hx, i)) 
                    tx = hx
                    ty = hy - 1
                if dir == 'D':
                    for i in range(ty - 1, hy, -1): 
                        set_of_pos[index + 1].add((hx, i)) 
                    tx = hx
                    ty = hy + 1
                if dir == 'S':
                    if hx > tx and hy > ty:
                        for i in range(0, deltax): 
                            set_of_pos[index + 1].add((tx + i, ty + i)) 
                        tx = hx - 1
                        ty = hy - 1 
                    if hx > tx and hy < ty:
                        for i in range(0, deltax): 
                            set_of_pos[index + 1].add((tx + i, ty - i)) 
                        tx = hx - 1
                        ty = hy + 1 
                    if hx < tx and hy > ty:
                        for i in range(0, deltax): 
                            set_of_pos[index + 1].add((tx - i, ty + i)) 
                        tx = hx + 1
                        ty = hy - 1 
                    if hx < tx and hy < ty:
                        for i in range(0, deltax): 
                            set_of_pos[index + 1].add((tx - i, ty - i)) 
                        tx = hx + 1
                        ty = hy + 1  
    positions[index] = (hx, hy)
    positions[index + 1] = (tx, ty) 
    if oldtx == tx:
        for i in range(min(oldty, ty), max(oldty, ty) + 1):
            set_of_pos[index + 1].add((tx, i))
    if oldty == ty:
        for i in range(min(oldtx, tx), max(oldtx, tx) + 1):
            set_of_pos[index + 1].add((i, ty))
    if index < 8:
        move_knot(index + 1, dir, 0) 
 
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    split_line = lines[i].split(" ")
    dir = split_line[0]
    step = int(split_line[1])
    for i in range(step):
        move_knot(0, dir, 1)
        
xpos = [pos[0] for pos in set_of_pos[9]]
ypos = [pos[1] for pos in set_of_pos[9]]
for r in range(max(ypos), min(ypos) - 1, -1):
    printstr = ""
    for c in range(min(xpos), max(xpos) + 1):
        if c == 0 and r == 0:
            printstr += "s"
            continue
        if (c, r) in set_of_pos[9]:
            printstr += "#"
        else:
            printstr += "."
            
print(len(set_of_pos[9]))