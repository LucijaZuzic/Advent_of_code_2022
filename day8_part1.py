file = open("input_day8.txt", "r")
lines = file.readlines() 
visible_up = []
visible_down = []
visible_right = []
visible_left = []
visible = []

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "") 
    visible_up.append([True for j in range(len(lines[i]))])
    visible_down.append([True for j in range(len(lines[i]))])
    visible_left.append([True for j in range(len(lines[i]))])
    visible_right.append([True for j in range(len(lines[i]))])
    visible.append([True for j in range(len(lines[i]))])

for i in range(len(lines)): 
    for j in range(len(lines[i])):
        h1 = int(lines[i][j])
        for k in range(j + 1, len(lines[i])):
            h2 = int(lines[i][k])
            if h1 >= h2:
                visible_left[i][k] = False
            if h1 <= h2:
                visible_right[i][j] = False 
        for k in range(i + 1, len(lines)):
            h2 = int(lines[k][j])
            if h1 >= h2:
                visible_up[k][j] = False
            if h1 <= h2:
                visible_down[i][j] = False
                
num_visible = 0
for i in range(len(lines)):
    string_print = ""
    for j in range(len(lines[i])):  
        visible[i][j] = visible_up[i][j] | visible_down[i][j] | visible_right[i][j]| visible_left[i][j]
        if visible[i][j]:
            string_print += "1"
            num_visible += 1
        else:
            string_print += "0"
    print(string_print) 
print(num_visible)