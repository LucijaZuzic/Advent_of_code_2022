file = open("input_day1.txt", "r")
lines = file.readlines()
elf = 0
elfs = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    if lines[i] != '':
        elf += int(lines[i]) 
    else:
        elfs.append(elf)
        elf = 0
elfs.append(elf)
elf = 0
elfs = sorted(elfs, reverse=True)
print(elfs[0] + elfs[1] + elfs[2])