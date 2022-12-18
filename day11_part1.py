file = open("input_day11.txt", "r")
lines = file.readlines()
monkey_num = 0
monkey_numbers = []
monkey_operations = []
monkey_test = []
monkey_true = []
monkey_false = []
monkey_inspected = []

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    if i % 7 == 1: 
        monkey_num += 1
        monkey_inspected.append(0)
        split_line = lines[i].replace("  Starting items: ", "").replace(",", "").split(" ")
        split_line = [int(num) for num in split_line]
        monkey_numbers.append(split_line)
    if i % 7 == 2:  
        split_line = lines[i].replace("  Operation: new = ", "").split(" ")
        monkey_operations.append(split_line)
    if i % 7 == 3:   
        split_line = lines[i].replace("  Test: divisible by ", "")
        monkey_test.append(int(split_line))
    if i % 7 == 4:   
        split_line = lines[i].replace("    If true: throw to monkey ", "")
        monkey_true.append(int(split_line))
    if i % 7 == 5:   
        split_line = lines[i].replace("    If false: throw to monkey ", "")
        monkey_false.append(int(split_line))

for k in range(20):
    for i in range(monkey_num):
        monkey_inspected[i] += len(monkey_numbers[i])
        for j in range(len(monkey_numbers[i])):
            new_num = monkey_numbers[i][j]
            second_param = 0
            if monkey_operations[i][2][0] == 'o':
                second_param = monkey_numbers[i][j]
            else:
                second_param = int(monkey_operations[i][2]) 
            if monkey_operations[i][1] == '+':
                new_num += second_param
            if monkey_operations[i][1] == '*':
                new_num *= second_param
            new_num = (new_num - new_num % 3) / 3
            if new_num % monkey_test[i] == 0:
                next_monkey = monkey_true[i]
            else:
                next_monkey = monkey_false[i]
            monkey_numbers[next_monkey].append(new_num)
        monkey_numbers[i] = []

sorted_inspect = sorted(monkey_inspected, reverse=True)
print(sorted_inspect[0] * sorted_inspect[1])