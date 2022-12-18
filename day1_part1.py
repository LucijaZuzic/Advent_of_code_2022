file = open("input_day1.txt", "r")
lines = file.readlines()
elf = 0
max_elf = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    if lines[i] != '':
        elf += int(lines[i]) 
    else:
        if elf > max_elf:
            max_elf = elf
        elf = 0
if elf > max_elf:
    max_elf = elf
elf = 0
print(max_elf)