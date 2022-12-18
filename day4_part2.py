file = open("input_day4.txt", "r")
lines = file.readlines()
fully_contained = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    comma = lines[i].find(',')
    first = lines[i][0:comma]
    first_line = first.find('-')
    start_first = int(first[0:first_line])
    end_first = int(first[first_line + 1:])
    second = lines[i][comma + 1:]
    second_line = second.find('-')
    start_second = int(second[0:second_line])
    end_second = int(second[second_line + 1:])
    if start_first >= start_second and start_first <= end_second:
        fully_contained += 1
    else:
        if start_second >= start_first and start_second <= end_first:
            fully_contained += 1
print(fully_contained)
