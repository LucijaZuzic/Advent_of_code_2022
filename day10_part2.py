file = open("input_day10.txt", "r") 
lines = file.readlines()
xval = 1
xvals = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")  
    xvals.append(xval)
    if lines[i][0] == 'a':
        xvals.append(xval)
        newxval = int(lines[i].split(" ")[1])
        xval += newxval
        
for i in range(0, 240, 40):
    strprint = ""
    for j in range(i, i + 40): 
        if abs(xvals[j] - j % 40) < 2: 
            strprint += "#"
        else:
            strprint += "."
    print(strprint)