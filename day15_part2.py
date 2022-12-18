file = open("input_day15.txt", "r")
dist_closest = []
lines = file.readlines()  
max_x = 0
max_y = 0
min_x = 0
min_y = 0
sensors = set()
sensors_filtered = set()
beacons = set() 
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    lines[i] = lines[i].replace("Sensor at ", "").replace(": closest beacon is at ", ", ")
    lines[i] = lines[i].replace("x=", "").replace("y=", "").split(", ")
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
    dist_closest.append(abs(lines[i][0] - lines[i][2]) + abs(lines[i][1] - lines[i][3]))
    max_x = max(max_x, lines[i][0] + dist_closest[-1])
    min_x = min(min_x, lines[i][0] - dist_closest[-1])
    max_y = max(max_y, lines[i][1] + dist_closest[-1])
    min_y = min(min_y, lines[i][1] - dist_closest[-1])
mintest = 0
maxtest = 4000000
def ranges_overlap(s1, e1, s0):
    s2 = mintest - s0
    e2 = maxtest - s0 
    if s1 >= s2 and s1 <= e2:
        return True
    if e1 >= s2 and e1 <= e2:
        return True
    if s2 >= s1 and s2 <= e1:
        return True
    if e2 >= s1 and e2 <= e1:
        return True
    return False
def merge_ranges(r1, r2): 
    s1 = r1[0]
    e1 = r1[1]
    s2 = r2[0]
    e2 = r2[1]
    if s1 >= s2 and s1 <= e2:
        return (min(s1, s2), max(e1, e2))
    if e1 >= s2 and e1 <= e2:
        return (min(s1, s2), max(e1, e2))
    if s2 >= s1 and s2 <= e1:
        return (min(s1, s2), max(e1, e2))
    if e2 >= s1 and e2 <= e1:
        return (min(s1, s2), max(e1, e2))
    if e1 == s2 - 1:
        return (min(s1, s2), max(e1, e2))
    if e2 == s1 - 1:
        return (min(s1, s2), max(e1, e2))
    return False

covered = dict()
for x in range(mintest - min_x, maxtest - min_x + 1):
    covered[x] = []
for i in range(len(lines)):
    lines[i][0] -= min_x
    lines[i][1] -= min_y
    lines[i][2] -= min_x
    lines[i][3] -= min_y
    sensors.add((lines[i][0], lines[i][1]))
    beacons.add((lines[i][2], lines[i][3])) 
    if ranges_overlap(lines[i][0] - dist_closest[i], lines[i][0] + dist_closest[i], min_x) and ranges_overlap(lines[i][1] - dist_closest[i], lines[i][1] + dist_closest[i], min_y):
        sensors_filtered.add((lines[i][0], lines[i][1], dist_closest[i]))
    if ranges_overlap(lines[i][0], lines[i][0], min_x) and ranges_overlap(lines[i][1], lines[i][1], min_y):
        covered[lines[i][0]].append((lines[i][1], lines[i][1]))
    if ranges_overlap(lines[i][2], lines[i][2], min_x) and ranges_overlap(lines[i][3], lines[i][3], min_y):
        covered[lines[i][2]].append((lines[i][3], lines[i][3]))
len2 = -1
for sensor in sensors_filtered:
    sensorx = sensor[0]
    sensory = sensor[1] 
    dist = sensor[2]  
    minimumx = sensorx - dist
    maximumx = sensorx + dist
    if minimumx < mintest - min_x:
        minimumx = mintest - min_x
    if maximumx > maxtest - min_x:
        maximumx = maxtest - min_x
    for x in range(minimumx, maximumx + 1):
        deltax = abs(x - sensorx) 
        deltay = dist - deltax
        minimumy = sensory - deltay
        maximumy = sensory + deltay 
        if minimumy < mintest - min_y:
            minimumy = mintest - min_y
        if maximumy > maxtest - min_y:
            maximumy = maxtest - min_y  
        covered[x].append((minimumy, maximumy))
for x in range(mintest - min_x, maxtest - min_x + 1):
    covered[x].sort()  
    index1 = 0
    while index1 < len(covered[x]):
        index2 = index1 + 1
        merged = True
        while index2 < len(covered[x]) and merged != False:
            first = covered[x][index1]
            second = covered[x][index2] 
            merged = merge_ranges(first, second) 
            if merged != False:
                covered[x][index1] = merged
                covered[x].remove(second)
                index1 = covered[x].index(merged) 
        index1 += 1 
    if len(covered[x]) > 1: 
        len2 = x
        print((len2 + min_x) * 4000000 + covered[len2][0][1] + 1 + min_y)
        break