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
beacons_not = set() 
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
max_y = max(max_y, 2000000)
min_y = min(min_y, 2000000)
y_test = 2000000 - min_y
for i in range(len(lines)):
    lines[i][0] -= min_x
    lines[i][1] -= min_y
    lines[i][2] -= min_x
    lines[i][3] -= min_y
    sensors.add((lines[i][0], lines[i][1]))
    beacons.add((lines[i][2], lines[i][3])) 
    if y_test >= lines[i][1] - dist_closest[i] and y_test <= lines[i][1] + dist_closest[i]:
        sensors_filtered.add((lines[i][0], lines[i][1], dist_closest[i]))
for sensor in sensors_filtered:
    sensorx = sensor[0]
    sensory = sensor[1] 
    dist = sensor[2] 
    deltay = abs(y_test - sensory)
    sgn2 = 1
    if y_test < sensory:
        sgn2 = -1 
    for deltax in range(dist - deltay + 1):
        for sgn1 in (-1, 1):
            point = (sensorx + deltax * sgn1, sensory + deltay * sgn2)
            if point not in sensors and point not in beacons: 
                beacons_not.add(point)   
print(len(beacons_not)) 