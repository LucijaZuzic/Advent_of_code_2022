file = open("input_day22.txt", "r")
lines = file.readlines()    

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

wide = max([len(line) for line in lines[:-2]])

mapa = []
for i in range(len(lines) - 2):
    mapa.append([])
    for j in range(wide):
        if j < len(lines[i]):
            mapa[-1].append(lines[i][j])
        else:
            mapa[-1].append(' ') 

begin_row = []
end_row = []
for i in range(len(lines) - 2): 
    first = -1
    last = 0
    for j in range(wide):
        if mapa[i][j] != ' ':
            last = j
            if first == -1:
                first = j
    begin_row.append(first)
    end_row.append(last)

begin_col = []
end_col = []
for j in range(wide):
    first = -1
    last = 0
    for i in range(len(lines) - 2): 
        if mapa[i][j] != ' ':
            last = i
            if first == -1:
                first = i
    begin_col.append(first)
    end_col.append(last)

moves = lines[-1]
amounts = moves.replace("R", "L").split("L")
for i in range(len(amounts)):
    amounts[i] = int(amounts[i])
directions = []
for char in moves:
    if char == 'R' or char == 'L':
        directions.append(char)

myy = 0
myx = begin_row[0]
mydir = 0

def rotate(movedir, mydir):
    if movedir == 'R':
        mydir += 90
    else:
        mydir -= 90
    mydir %= 360
    return mydir

def mapprint():
    for i in range(len(lines) - 2): 
        strp = ""
        for j in range(wide):
            strp += mapa[i][j]
        print(strp)

mapprint()
for i in range(len(amounts)):
    for j in range(amounts[i]):
        #print(myy, myx, mydir)
        if mydir == 0:
            mapa[myy][myx] = '>'
        if mydir == 90:
            mapa[myy][myx] = 'v'
        if mydir == 180:
            mapa[myy][myx] = '<'
        if mydir == 270:
            mapa[myy][myx] = '^'
        if mydir == 0:
            newx = myx + 1
            if newx > end_row[myy]:
                newx = begin_row[myy]
            if mapa[myy][newx] != '#':
                myx = newx
            else:
                break 
        if mydir == 90:
            newy = myy + 1
            if newy > end_col[myx]:
                newy = begin_col[myx]
            if mapa[newy][myx] != '#':
                myy = newy
            else:
                break 
        if mydir == 180:
            newx = myx - 1
            if newx < begin_row[myy]:
                newx = end_row[myy]
            if mapa[myy][newx] != '#':
                myx = newx
            else:
                break 
        if mydir == 270:
            newy = myy - 1
            if newy < begin_col[myx]:
                newy = end_col[myx]
            if mapa[newy][myx] != '#':
                myy = newy
            else:
                break 
    if i < len(directions):
        mydir = rotate(directions[i], mydir)
mapprint()
print(1000 * (myy + 1) + 4 * (myx + 1) + int(mydir / 90))