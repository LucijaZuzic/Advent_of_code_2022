file = open("input_day9.txt", "r") 
hx = 0
hy = 0
tx = 0
ty = 0
set_tpos = set()
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    split_line = lines[i].split(" ")
    dir = split_line[0]
    step = int(split_line[1])
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
    if deltax > 1 or deltay > 1:
        if hx == tx:
            if ty < hy:
                for i in range(ty, hy):
                    set_tpos.add((tx, i))
                ty = hy - 1
            if ty > hy:
                for i in range(ty, hy, -1):
                    set_tpos.add((tx, i))
                ty = hy + 1
        else:
            if hy == ty:
                if tx < hx:
                    for i in range(tx, hx):
                        set_tpos.add((i, ty))
                    tx = hx - 1
                if tx > hx:
                    for i in range(tx, hx, -1):
                        set_tpos.add((i, ty))
                    tx = hx + 1
            else:
                if dir == 'R':
                    for i in range(tx + 1, hx):
                        set_tpos.add((i, hy))
                    tx = hx - 1
                    ty = hy
                if dir == 'L':
                    for i in range(tx - 1, hx, -1):
                        set_tpos.add((i, hy))
                    tx = hx + 1
                    ty = hy
                if dir == 'U':
                    for i in range(ty + 1, hy):
                        set_tpos.add((hx, i))
                    tx = hx
                    ty = hy - 1
                if dir == 'D':
                    for i in range(ty - 1, hy, -1):
                        set_tpos.add((hx, i))
                    tx = hx
                    ty = hy + 1
print(len(set_tpos))