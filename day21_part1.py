file = open("input_day21.txt", "r")
lines = file.readlines()   
monkeys = dict()
calculated = dict()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").split(": ")
    name = lines[i][0]
    operation = lines[i][1] 
    if ord(operation[0]) >= ord('0') and ord(operation[0]) <= ord('9'):
        calculated[name] = int(operation)
    else:
        monkeys[name] = operation.split(" ")
 
def round():
    for monkey in monkeys:
        operation = monkeys[monkey] 
        if operation[0] in calculated:
            operation[0] = calculated[operation[0]]
            monkeys[monkey] = operation
        if operation[2] in calculated:
            operation[2] = calculated[operation[2]]
            monkeys[monkey] = operation 
    for monkey in monkeys:
        operation = monkeys[monkey] 
        if type(operation[0]) == int and type(operation[2]) == int:
            if operation[1] == '+':
                calculated[monkey] = int(operation[0]) + int(operation[2])
            if operation[1] == '*':
                calculated[monkey] = int(operation[0]) * int(operation[2])
            if operation[1] == '-':
                calculated[monkey] = int(operation[0]) - int(operation[2])
            if operation[1] == '/':
                calculated[monkey] = int(int(operation[0]) / int(operation[2]))
    for monkey in calculated:
        if monkey in monkeys:
            monkeys.pop(monkey) 

iter = 0
while len(monkeys) != 0:
    round()
    iter += 1
 
print(calculated['root'])