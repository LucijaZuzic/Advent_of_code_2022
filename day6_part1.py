file = open("input_day6.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    for j in range(len(lines[i])):
        packet = lines[i][j:j+4]
        valid = len(packet) == 4
        if valid:
            for char in packet:
                if packet.count(char) > 1:
                    valid = False
                    break
            if valid:
                print(j + 4)
                break