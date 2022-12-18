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
suma = 0
for i in range(20, 260, 40):
    print(xvals[i - 1], i, xvals[i - 1] * i)
    suma += xvals[i - 1] * i
print(suma)