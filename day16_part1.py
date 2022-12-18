file = open("test_day16.txt", "r")
lines = file.readlines()
valve_flow = dict()
valve_neighbours = dict() 
max_steps = 30 

def travel(valve, steps, score, open): 
    print(valve, steps, score, max_steps, open)
    if steps >= max_steps:
        return score
    add_score = 0
    for valve_new in open:
        if open[valve_new]:
            add_score += valve_flow[valve_new]
    score += add_score
    added = False
    if open[valve] == False and valve_flow[valve] > 0:
        score += add_score
        steps += 1
        added = True
    open[valve] = True
    retval = 0
    for neighbour in valve_neighbours[valve]:
        new_open = dict()
        for valve_new in open:
            new_open[valve_new] = open[valve_new]
        retval = max(retval, travel(neighbour, steps + 1, score, new_open)) 
    return retval
 
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").replace("has flow rate=", "").replace("Valve ", "").replace(",", "")
    lines[i] = lines[i].replace("; tunnels lead to valves", "")
    lines[i] = lines[i].replace("; tunnels lead to valve", "")
    lines[i] = lines[i].replace("; tunnel leads to valves", "")
    lines[i] = lines[i].replace("; tunnel leads to valve", "")
    lines[i] = lines[i].split(" ")
    print(lines[i])
    valve_flow[lines[i][0]] = int(lines[i][1])  
    valve_neighbours[lines[i][0]] = []
    for j in range(2, len(lines[i])):
        valve_neighbours[lines[i][0]].append(lines[i][j])

first_open = dict()
for valve in valve_flow:
    first_open[valve] = False

print(travel('AA', 0, 1, first_open))