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

def segmentprint():
    for i in range(len(lines) - 2): 
        strp = ""
        for j in range(wide):
            strp += str(getSegment(j, i))
        print(strp)

def getSegment(x, y):
    if x < 50:
        if y < 100:
            return 0
        if y < 150:
            return 5 
        return 6
    if x < 100:
        if y < 50:
            return 2
        if y < 100:
            return 1
        if y < 150:
            return 4
        return 0
    if y < 100:
        return 3
    return 0

def appear(x, y, direc):
    retx = x
    rety = y
    retdir = direc
    mysegment = getSegment(x, y)
    if mysegment == 1:
        if direc == 0:
            retx = 50 + y
            rety = 49
            retdir = 270
        if direc == 90:
            retx = x
            rety = y + 1
            retdir = direc
        if direc == 180:
            retx = y - 50
            rety = 100
            retdir = 90
        if direc == 270:
            retx = x
            rety = y - 1
            retdir = direc
    if mysegment == 2:
        if direc == 0:
            retx = x + 1
            rety = y
            retdir = direc
        if direc == 90:
            retx = x  
            rety = y + 1
            retdir = direc
        if direc == 180:
            retx = 0
            rety = 149 - y 
            retdir = 0
        if direc == 270:
            retx = 0
            rety = 249 - x
            retdir = 0
    if mysegment == 3:
        if direc == 0:
            retx = 99
            rety = 149 - y
            retdir = 180
        if direc == 90:
            retx = 99
            rety = x - 50
            retdir = 180
        if direc == 180:
            retx = x - 1 
            rety = y  
            retdir = direc
        if direc == 270:
            retx = x - 100
            rety = 199
            retdir = 270
    if mysegment == 4:
        if direc == 0:
            retx = 99
            rety = 150 - y
            retdir = 180
        if direc == 90:
            retx = 49
            rety = x + 100
            retdir = 180
        if direc == 180:
            retx = x - 1 
            rety = y  
            retdir = direc
        if direc == 270:
            retx = x
            rety = y - 1
            retdir = direc
    if mysegment == 5:
        if direc == 0:
            retx = x + 1
            rety = y
            retdir = direc
        if direc == 90:
            retx = x  
            rety = y + 1
            retdir = direc
        if direc == 180:
            retx = 50
            rety = 149 - y
            retdir = 0
        if direc == 270: 
            retx = 50
            rety = x + 50 
            retdir = 0 
    if mysegment == 6:
        if direc == 0:
            retx = y - 100
            rety =  149
            retdir = 270
        if direc == 90:
            retx = x + 100
            rety = 0
            retdir = 90
        if direc == 180:
            retx = 249 - y
            rety = 0 
            retdir = 90
        if direc == 270:
            retx = x
            rety = y - 1
            retdir = direc
    return retx, rety, retdir
 
nummove = 0
mapprint()
for i in range(len(amounts)):
    if (mapa[myy][myx] == ' '):
        print("ERR", myy, myx, mydir, i)
        break
    for j in range(amounts[i]):
        if (mapa[myy][myx] == ' '):
            print("ERR", myy, myx, mydir, i)
            break
        if mydir == 0:
            mapa[myy][myx] = '>'
        if mydir == 90:
            mapa[myy][myx] = 'v'
        if mydir == 180:
            mapa[myy][myx] = '<'
        if mydir == 270:
            mapa[myy][myx] = '^'
        nummove += 1
        nummove %= 10
        mapa[myy][myx] = str(nummove)
        if mydir == 0:
            newx = myx + 1
            newy = myy
            newdir = mydir
            if newx > end_row[myy]:
                print("Diving", myy, myx, mydir)
                newx, newy, newdir = appear(myx, myy, mydir)
                print("Emerging", newy, newx, newdir)
            if mapa[myy][newx] != '#':
                myx = newx
                myy = newy
                mydir = newdir
            else:
                break 
        if mydir == 90:
            newx = myx
            newy = myy + 1
            newdir = mydir
            if newy > end_col[myx]:
                print("Diving", myy, myx, mydir)
                newx, newy, newdir = appear(myx, myy, mydir)
                print("Emerging", newy, newx, newdir)
            if mapa[newy][myx] != '#':
                myx = newx
                myy = newy
                mydir = newdir
            else:
                break 
        if mydir == 180:
            newx = myx - 1
            newy = myy
            newdir = mydir
            if newx < begin_row[myy]:
                print("Diving", myy, myx, mydir)
                newx, newy, newdir = appear(myx, myy, mydir)
                print("Emerging", newy, newx, newdir)
            if mapa[myy][newx] != '#':
                myx = newx
                myy = newy
                mydir = newdir
            else:
                break 
        if mydir == 270:
            newx = myx
            newy = myy - 1
            newdir = mydir
            if newy < begin_col[myx]:
                print("Diving", myy, myx, mydir)
                newx, newy, newdir = appear(myx, myy, mydir)
                print("Emerging", newy, newx, newdir)
            if mapa[newy][myx] != '#':
                myx = newx
                myy = newy
                mydir = newdir
            else:
                break 
    if i < len(directions):
        mydir = rotate(directions[i], mydir)  
print(1000 * (myy + 1) + 4 * (myx + 1) + int(mydir / 90))