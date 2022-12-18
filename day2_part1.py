file = open("input_day2.txt", "r")
lines = file.readlines()
dict_points_me = {'X': 1, 'Y': 2, 'Z': 3}
dict_points_other = {'A': 1, 'B': 2, 'C': 3}
dict_victory = {1: 3, 3: 2, 2: 1}
points = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    other = lines[i][0]
    me = lines[i][2]
    my_points = dict_points_me[me]
    other_points = dict_points_other[other]
    points += my_points
    if dict_victory[my_points] == other_points:
        points += 6
    if my_points == other_points:
        points += 3
print(points)