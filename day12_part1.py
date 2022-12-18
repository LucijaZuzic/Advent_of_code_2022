file = open("input_day12.txt", "r")
lines = file.readlines()
start = (0, 0)
end = (0, 0)
heights = [[-1 for j in range(len(lines[i]))] for i in range(len(lines))]
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            start = (i, j)
            heights[i][j] = ord('a') - ord('a')
        else:
            if lines[i][j] == 'E':
                end = (i, j)
                heights[i][j] = ord('z') - ord('a')
            else:
                heights[i][j] = ord(lines[i][j]) - ord('a')

min_dist = [[len(lines[i]) * len(lines) + 1 for j in range(len(lines[i]))] for i in range(len(lines))]

queue = []
min_dist[start[0]][start[1]] = 0
queue.append((0, start))
x = 0
while len(queue) != 0:
    x += 1
    old_dist = queue[0][0]
    current = queue[0][1] 
    queue.remove((old_dist, current))
    for xdist in (-1, 0, 1):
        for ydist in (-1, 0, 1):
            if (xdist == 0 and ydist == 0) or (xdist != 0 and ydist != 0):
                continue
            neighbour = (current[0] + xdist, current[1] + ydist)
            if neighbour[0] < 0 or neighbour[0] >= len(lines) or neighbour[1] < 0 or neighbour[1] >= len(lines[0]):
                continue
            diff = heights[neighbour[0]][neighbour[1]] - heights[current[0]][current[1]]
            if diff > 1:
                continue
            else:
                new_dist = old_dist + 1
                if new_dist < min_dist[neighbour[0]][neighbour[1]]:
                    min_dist[neighbour[0]][neighbour[1]] = new_dist
                    queue.append((new_dist, neighbour)) 
                    queue.sort()  
print(min_dist[end[0]][end[1]])