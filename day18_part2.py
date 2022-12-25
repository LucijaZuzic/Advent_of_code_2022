file = open("input_day18.txt", "r")
cubes = set()
lines = file.readlines()  
visited = set()
sides = set()
surface = 0

maxx = 0
maxy = 0
maxz = 0
minx = 0
miny = 0
minz = 0

def fill(x, y, z):  
    visited.add((x, y, z))
    for offset in (-1, 1):
        if (x + offset, y, z) not in cubes:
            if (x + offset, y, z) not in visited:
                if x + offset >= minx - 1 and  x + offset <= maxx + 1:
                    fill(x + offset, y, z) 
        else:
            sides.add((x + offset, y, z, "x", offset))
        if (x, y + offset, z) not in cubes:
            if (x, y + offset, z) not in visited:
                if y + offset >= miny - 1 and  y + offset <= maxy + 1:
                    fill(x, y + offset, z) 
        else:
            sides.add((x, y + offset, z, "y", offset))
        if (x, y, z + offset) not in cubes:
            if (x, y, z + offset) not in visited:
                if z + offset >= minz - 1 and  z + offset <= maxz + 1:
                    fill(x, y, z + offset) 
        else:
            sides.add((x, y, z + offset, "z", offset))

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "") 
    lines[i] = lines[i].split(",")
    cube = (int(lines[i][0]), int(lines[i][1]), int(lines[i][2]))
    cubes.add(cube)
    if i == 0:
        maxx = cube[0]
        maxy = cube[1]
        maxz = cube[2] 
        minx = cube[0]
        miny = cube[1]
        minz = cube[2] 
    else:
        maxx = max(maxx, cube[0])
        maxy = max(maxy, cube[1])
        maxz = max(maxz, cube[2])
        minx = min(minx, cube[0])
        miny = min(miny, cube[1])
        minz = min(minz, cube[2]) 

adj = set() 

for cube in cubes: 
    x = cube[0]
    y = cube[1]
    z = cube[2]
    for offset in (-1, 1):
        if (x + offset, y, z) not in cubes:
            adj.add((x + offset, y, z))
        if (x, y + offset, z) not in cubes:
            adj.add((x, y + offset, z))
        if (x, y, z + offset) not in cubes:
            adj.add((x, y, z + offset)) 
     
#fill(minx - 1, miny - 1, minz - 1)

queue = []
queue.append((minx - 1, miny - 1, minz - 1)) 

while len(queue) != 0:
    cube = queue[-1]
    x = cube[0]
    y = cube[1]
    z = cube[2]
    visited.add((x, y, z))
    for offset in (-1, 1):
        if (x + offset, y, z) not in cubes:
            if (x + offset, y, z) not in visited:
                if x + offset >= minx - 1 and x + offset <= maxx + 1:
                    queue.append((x + offset, y, z))
        else:
            sides.add((x + offset, y, z, "x", offset))
        if (x, y + offset, z) not in cubes:
            if (x, y + offset, z) not in visited:
                if y + offset >= miny - 1 and y + offset <= maxy + 1:
                    queue.append((x, y + offset, z))
        else:
            sides.add((x, y + offset, z, "y", offset))
        if (x, y, z + offset) not in cubes:
            if (x, y, z + offset) not in visited:
                if z + offset >= minz - 1 and z + offset <= maxz + 1:
                    queue.append((x, y, z + offset))
        else:
            sides.add((x, y, z + offset, "z", offset))
    queue.remove(cube)
print(len(sides))