file = open("input_day14.txt", "r")
lines = file.readlines() 
min_x = 500
max_x = 500
min_y = 0
max_y = 0
new_lines = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").split(" -> ")
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].split(",")
        for k in range(len(lines[i][j])):
            lines[i][j][k] = int(lines[i][j][k])
        max_x = max(max_x, lines[i][j][0])
        max_y = max(max_y, lines[i][j][1])
        min_x = min(min_x, lines[i][j][0])
        min_y = min(min_y, lines[i][j][1])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j][0] -= min_x
        lines[i][j][1] -= min_y

xoffset = 0
max_x += 1
max_y += 1
if 500 - min_x < max_y - min_y:
    xoffset = max_y - min_y - (500 - min_x)
if max_x - 500 < max_y - min_y:
    max_x += max_y - min_y - (max_x - 500)
map = [['.' for j in range(max_x - min_x + 1 + xoffset)] for i in range(max_y - min_y + 1)]
def print_map():
    for y in range(max_y - min_y + 1):
        strp = ""
        for x in range(max_x - min_x + 1 + xoffset):
            strp += map[y][x]
        print(strp)
for i in range(len(lines)):
    for j in range(len(lines[i]) - 1):
        current_x = lines[i][j][0]
        current_y = lines[i][j][1]
        next_x = lines[i][j + 1][0]
        next_y = lines[i][j + 1][1]
        dirx = 1
        diry = 1
        if next_x < current_x:
            dirx = -1
        if next_y < current_y:
            diry = -1
        for y in range(current_y, next_y + diry, diry):
            for x in range(current_x, next_x + dirx, dirx):
                map[y][x + xoffset] = '#'   
def add_sand():
    sy = 0 - min_y
    sx = 500 - min_x + xoffset
    new_sx = sx
    new_sy = sy
    map[sy][sx] = '+'
    at_rest = False 
    while not at_rest:
        if sy < len(map) - 1 and map[sy + 1][sx] == '.':
            new_sx = sx
            new_sy = sy + 1
        else:
            if sx > 0 and sy < len(map) - 1 and map[sy + 1][sx - 1] == '.':
                new_sx = sx - 1
                new_sy = sy + 1
            else:
                if sx < len(map[0]) - 1 and sy < len(map) - 1 and map[sy + 1][sx + 1] == '.':
                    new_sx = sx + 1
                    new_sy = sy + 1 
        map[sy][sx] = '.'
        if sx == new_sx and sy == new_sy:
            at_rest = True
            map[new_sy][new_sx] = 'o'
        else:
            map[new_sy][new_sx] = '+'
        sx = new_sx
        sy = new_sy
    if sx == 500 - min_x + xoffset and sy == 0 - min_y:
        return False
    else:
        return True
num_cells = 0
all_at_rest = True
while all_at_rest:
    num_cells += 1
    all_at_rest = add_sand()
print(num_cells)  