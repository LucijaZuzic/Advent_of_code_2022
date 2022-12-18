file = open("test_day16.txt", "r")
lines = file.readlines()
valve_flow = dict()
valve_neighbours = dict() 
max_steps = 3000
max_flow = 1
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").replace("has flow rate=", "").replace("Valve ", "").replace(",", "")
    lines[i] = lines[i].replace("; tunnels lead to valves", "")
    lines[i] = lines[i].replace("; tunnels lead to valve", "")
    lines[i] = lines[i].replace("; tunnel leads to valves", "")
    lines[i] = lines[i].replace("; tunnel leads to valve", "")
    lines[i] = lines[i].split(" ")
    print(lines[i])
    valve_flow[lines[i][0]] = int(lines[i][1]) 
    if valve_flow[lines[i][0]] != 0:
        max_flow = abs(max_flow * valve_flow[lines[i][0]])
    valve_neighbours[lines[i][0]] = []
    for j in range(2, len(lines[i])):
        valve_neighbours[lines[i][0]].append(lines[i][j])

prev = dict() 
numsteps = dict() 
for valve in valve_flow:
    prev[valve] = []  
    numsteps[valve] = max_flow * max_flow
    
queue = [] 
numsteps["AA"] = 0
queue.append((0, "AA"))

while len(queue) != 0:
    current = queue[0] 
    if numsteps[current[1]] < max_steps:
        for valve in valve_neighbours[current[1]]: 
            if current[1] in prev[valve]:
                continue
            if valve in prev[current[1]]:
                continue
            if numsteps[valve] > numsteps[current[1]] + 1: 
                if (numsteps[valve], valve) in queue:
                    queue.remove((numsteps[valve], valve)) 
                prev[valve] = [] 
                for ancestor in prev[current[1]]:
                    prev[valve].append(ancestor)
                prev[valve].append(current[1])
                numsteps[valve] = numsteps[current[1]] + 1
                if numsteps[valve] < max_steps:
                    queue.append((numsteps[valve], valve)) 
    if current in queue:
        queue.remove(current) 
    queue.sort()
    print(queue)
 
print(numsteps) 
print(prev) 
'''
current = min_valve
max_flow = 1
print(current)
while current != 'AA' and prev[current] != '':
    if valve_flow[current] != 0:
        max_flow *= - valve_flow[current]
    current = prev[current]
    print(current)
print(max_flow)
'''


