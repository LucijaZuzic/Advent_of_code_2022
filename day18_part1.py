file = open("input_day18.txt", "r")
cubes = set()
lines = file.readlines()  
surface = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "") 
    lines[i] = lines[i].split(",")
    cubes.add((int(lines[i][0]), int(lines[i][1]), int(lines[i][2])))
for cube in cubes:
    exposed = 6
    x = cube[0]
    y = cube[1]
    z = cube[2]
    for offset in (-1, 1):
        if (x + offset, y, z) in cubes:
            exposed -= 1
        if (x, y + offset, z) in cubes:
            exposed -= 1
        if (x, y, z + offset) in cubes:
            exposed -= 1
    surface += exposed 
print(surface)