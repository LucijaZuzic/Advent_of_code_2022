file = open("test_day23.txt", "r")
lines = file.readlines()    
elves = set()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            elves.add((j, i))

def propose(elf, round):
    x = elf[0]
    y = elf[1]
    north = 0
    south = 0
    west = 0
    east = 0
    for dx in range(-1,2,1):
        for dy in range(-1,2,1):
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            neighbour = (nx, ny)
            if dy == -1 and neighbour in elves:
                north += 1
            if dy == 1 and neighbour in elves:
                south += 1
            if dx == -1 and neighbour in elves:
                west += 1
            if dx == 1 and neighbour in elves:
                east += 1
    if north + south + east + west == 0:
        return (x, y)
    if round % 4 == 0:
        if north == 0:
            return (x, y - 1)
        if south == 0:
            return (x, y + 1)
        if west == 0:
            return (x - 1, y)
        if east == 0:
            return (x + 1, y)
    if round % 4 == 1:
        if south == 0:
            return (x, y + 1)
        if west == 0:
            return (x - 1, y)
        if east == 0:
            return (x + 1, y)
        if north == 0:
            return (x, y - 1)
    if round % 4 == 2:
        if west == 0:
            return (x - 1, y)
        if east == 0:
            return (x + 1, y)
        if north == 0:
            return (x, y - 1)
        if south == 0:
            return (x, y + 1)
    if round % 4 == 3:
        if east == 0:
            return (x + 1, y)
        if north == 0:
            return (x, y - 1)
        if south == 0:
            return (x, y + 1)
        if west == 0:
            return (x - 1, y)
    return (x, y) 

def printMap():
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    empty = 0
    for elf in elves:
        x = elf[0]
        y = elf[1]
        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
    for j in range(ymin, ymax + 1): 
        for i in range(xmin, xmax + 1):
            if (i, j) not in elves: 
                empty += 1 
    print(empty)

num_rounds = 10

for round in range(num_rounds): 
    from_to = []
    num_proposed = dict()
    for elf in elves:
        retval = propose(elf, round) 
        from_to.append((elf, retval))
        if retval in num_proposed:
            num_proposed[retval] += 1
        else:
            num_proposed[retval] = 1
    new_elves = set()
    for proposition in from_to:
        from_pos = proposition[0]
        to_pos = proposition[1]
        if num_proposed[to_pos] == 1:
            new_elves.add(to_pos)
        else:
            new_elves.add(from_pos)
    elves.clear() 
    for elf in new_elves:
        elves.add(elf)

printMap()