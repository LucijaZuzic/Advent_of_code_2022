file = open("input_day2.txt", "r")
lines = file.readlines()
dict_outcome = {'X': 0, 'Y': 3, 'Z': 6}
dict_points_other = {'A': 1, 'B': 2, 'C': 3}
dict_victory = {1: 3, 3: 2, 2: 1}
dict_loss = {3: 1, 2: 3, 1: 2}
points = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    other = lines[i][0]
    me = lines[i][2]
    outcome = dict_outcome[me]
    other_points = dict_points_other[other]
    points += outcome
    if outcome == 0:
        points += dict_victory[other_points]
    if outcome == 3:
        points += other_points
    if outcome == 6:
        points += dict_loss[other_points]
print(points)