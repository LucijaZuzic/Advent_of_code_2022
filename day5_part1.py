file = open("input_day5.txt", "r")
lines = file.readlines()
starting_index = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    if len(lines[i]) > 0 and lines[i][1] == '1':
        starting_index = i - 1
        numlines = int(lines[i].split(" ")[-2])
boxes = []
for i in range(numlines):
    boxes.append([])
for i in range(starting_index, -1, -1):
    index = 0
    for j in range(0, len(lines[i]), 4):
        character = lines[i][j:j + 3][1:-1]
        if character != " ":
            boxes[index].append(lines[i][j:j + 3][1:-1])
        index += 1
for i in range(starting_index + 3, len(lines)):
    numbers = lines[i].replace("move ", "").replace(" from ", " ").replace(" to ", " ").split(" ")
    numboxes = int(numbers[0])
    frombox = int(numbers[1]) - 1
    tobox = int(numbers[2]) - 1
    for j in range(numboxes):
        box = boxes[frombox][-1]
        boxes[frombox].pop()
        boxes[tobox].append(box)
boxtop = ""
for i in range(numlines):
    boxtop += boxes[i][-1]
print(boxtop)