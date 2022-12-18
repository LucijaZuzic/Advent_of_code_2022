file = open("input_day3.txt", "r")
lines = file.readlines()
priority = 0
for i in range(0, len(lines), 3):
    lines[i] = lines[i].replace("\n", "")
    lines[i + 1] = lines[i + 1].replace("\n", "")
    lines[i + 2] = lines[i + 2].replace("\n", "")
    first = lines[i] 
    second = lines[i + 1] 
    third = lines[i + 2] 
    for c in first:
        if second.count(c) != 0:
            if third.count(c) != 0:
                ascii_sign = ord(c)
                if ascii_sign >= ord('a') and ascii_sign <= ord('z'):
                    priority += ascii_sign - ord('a') + 1
                else:
                    priority += ascii_sign - ord('A') + 27
                break
print(priority)