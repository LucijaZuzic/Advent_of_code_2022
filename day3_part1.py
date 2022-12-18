file = open("input_day3.txt", "r")
lines = file.readlines()
priority = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    first = lines[i][0:int(len(lines[i]) / 2)]
    second = lines[i][int(len(lines[i]) / 2):]
    for c in first:
        if second.count(c) != 0:
            ascii_sign = ord(c)
            if ascii_sign >= ord('a') and ascii_sign <= ord('z'):
                priority += ascii_sign - ord('a') + 1
            else:
                priority += ascii_sign - ord('A') + 27
            break
print(priority)