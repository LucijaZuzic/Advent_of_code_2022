file = open("input_day8.txt", "r")
lines = file.readlines() 
distance_up = []
distance_down = []
distance_right = []
distance_left = []
score = []

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "") 
    distance_up.append([0 for j in range(len(lines[i]))])
    distance_down.append([0 for j in range(len(lines[i]))])
    distance_right.append([0 for j in range(len(lines[i]))])
    distance_left.append([0 for j in range(len(lines[i]))])
    score.append([0 for j in range(len(lines[i]))])

for i in range(len(lines)): 
    for j in range(len(lines[i])):
        h1 = int(lines[i][j])
        for k in range(j - 1, -1, -1):
            h2 = int(lines[i][k]) 
            distance_left[i][j] = j - k 
            if h1 <= h2:
                break
        for k in range(j + 1, len(lines[i])):
            h2 = int(lines[i][k]) 
            distance_right[i][j] = k - j 
            if h1 <= h2:
                break
        for k in range(i - 1, -1, -1):
            h2 = int(lines[k][j]) 
            distance_up[i][j] = i - k
            if h1 <= h2:
                break
        for k in range(i + 1, len(lines)):
            h2 = int(lines[k][j]) 
            distance_down[i][j] = k - i
            if h1 <= h2:
                break
                
max_score = 0
for i in range(len(lines)):
    string_print = ""
    for j in range(len(lines[i])):  
        score[i][j] = distance_up[i][j] * distance_down[i][j] * distance_left[i][j] * distance_right[i][j] 
        max_score = max(max_score, score[i][j])
        string_print += str(score[i][j])
    print(string_print) 
print(max_score)