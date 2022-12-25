file = open("input_day21.txt", "r")
lines = file.readlines()   
monkeys = dict()
calculated = dict()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").split(": ")
    name = lines[i][0]
    operation = lines[i][1] 
    if name == 'humn':
        continue
    if ord(operation[0]) >= ord('0') and ord(operation[0]) <= ord('9'):
        calculated[name] = int(operation)
    else:
        operation = operation.split(" ")
        if name == 'root':
            operation[1] = '='
        monkeys[name] = operation
 
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
while len(monkeys) != 0 and iter < 1666:
    round()
    iter += 1 

def deepDive(monkey):
    if type(monkey) == int:
        return str(monkey)
    if monkey in calculated:
        return str(calculated[monkey])
    if monkey == 'humn':
        return 'humn'
    operation = monkeys[monkey] 
    val1 = deepDive(operation[0])
    val2 = deepDive(operation[2]) 

    if operation[1] == '+' or operation[1] == '-':
        return "(" + val1 + operation[1] + val2 + ")"
    else:
        return "(" + val1 + operation[1] + val2 + ")"

operations = deepDive('root') 

def shorter_rest(rest, repl):
    index = rest.find("humn")
    before = rest[:index]
    after = rest[index+4:]
    if index != 1:
        op = rest[index-1]
        begin = index-2 
        while ord(rest[begin - 1]) >= ord('0') and ord(rest[begin - 1]) <= ord('9'):
            begin -= 1
        num = rest[begin:index-1] 
    else:
        op = rest[index+4]
        end = index+6
        while ord(rest[end + 1]) >= ord('0') and ord(rest[end + 1]) <= ord('9'):
            begin -= 1
        num = rest[index+5:end]
   # print(op, num, before, after, repl)
    #if ord(repl[0]) >= ord('0') and ord(repl[0]) <= ord('9'):
        #print(eval(repl + rest.replace('humn', '1')))
    #if ord(repl[len(repl)- 1]) >= ord('0') and ord(repl[len(repl)- 1]) <= ord('9'):
        #print(eval(rest.replace('humn', '1') + repl))

def calc(operations, index):
    first = []
    last = []
    for i in range(len(operations)):
        if operations[i] == '(':
            first.append(i)
    for i in range(len(operations) - 1, -1, -1):
        if operations[i] == ')':
            last.append(i)
    larger = operations[first[-index-1]:last[-index-1]+1]
    smaller = operations[first[-index]+1:last[-index]]    
    if ord(smaller[0]) >= ord('0') and ord(smaller[0]) <= ord('9'):
        lower = 0
        upper = 0
        while (ord(smaller[upper + 1]) >= ord('0') and ord(smaller[upper + 1]) <= ord('9')) or smaller[upper + 1] == '.':
            upper += 1
    if ord(smaller[len(smaller) - 1]) >= ord('0') and ord(smaller[len(smaller) - 1]) <= ord('9'):
        lower = len(smaller) - 1
        upper = len(smaller) - 1
        while (ord(smaller[lower - 1]) >= ord('0') and ord(smaller[lower - 1]) <= ord('9')) or smaller[lower - 1] == '.':
            lower -= 1
    old_str = smaller[lower:upper+1]
    old_num = float(old_str)
    if upper == len(smaller) - 1:
        rest = smaller[:lower-2]
    else:
        rest = smaller[upper+2:]
    #print(larger)
    #print(smaller)
    #print(old_num, rest)
    if ord(larger[1]) >= ord('0') and ord(larger[1]) <= ord('9'):
        repl = operations[first[-index-1]+1:first[-index]]
        mul = float(operations[first[-index-1]+1:first[-index]-1])
        op = operations[first[-index]-1]
        if op == '-':
            res = mul - old_num
        if op == '/':
            res = mul / old_num
        if op == '+':
            res = mul + old_num
        if op == '*':
            res = mul * old_num
        if op == '/' or op == '*':
            new_rest = "(" + repl + rest + ")" 
            shorter_rest(rest, repl)
            index += 1
        else:
            if op == '+':
                new_rest = rest
            else:
                new_rest = "-(" + rest + ")" 
                index += 1
    if ord(larger[len(larger) - 2]) >= ord('0') and ord(larger[len(larger) - 2]) <= ord('9'): 
        repl = operations[last[-index]+1:last[-index-1]] 
        mul = float(operations[last[-index]+2:last[-index-1]])
        op = operations[last[-index]+1]
        if op == '-':
            res = old_num - mul
        if op == '/':
            res = old_num / mul
        if op == '+':
            res = old_num + mul
        if op == '*':
            res = old_num + mul  
            res = mul * old_num
        if op == '/' or op == '*':
            new_rest = "(" + rest + repl + ")" 
            shorter_rest(rest, repl)
            index += 1
        else:
            new_rest = rest
    #print(repl, mul, op)
    if upper == len(smaller) - 1:
        new_smaller = smaller.replace(rest + smaller[lower-2] + old_str, new_rest + smaller[lower-2] + str(res))
    else:
        new_smaller = smaller.replace(old_str + smaller[upper+1] + rest, str(res) + smaller[upper+1] + new_rest)
    if ord(larger[1]) >= ord('0') and ord(larger[1]) <= ord('9'):
        new_larger = larger.replace(repl + "(" + smaller + ")", new_smaller)
    if ord(larger[len(larger) - 2]) >= ord('0') and ord(larger[len(larger) - 2]) <= ord('9'): 
        new_larger = larger.replace("(" + smaller + ")" + repl, new_smaller)
    new_operations = operations.replace(larger, new_larger)
    #print(new_smaller)
    print(larger, new_larger)
    #print(new_operations)
    return new_operations, index

'''
index = 1 
for i in range(40):
    operations, index = calc(operations, index)    
'''

index = operations.find("=")
equality_check = operations.replace("=", "==")
no_end = operations[:index] + ")"
number_to_match = eval(operations[index+1:-1])
number = number_to_match
'''
for i in range(int(number_to_match / 19.11485266605), int(number_to_match / 19.11485266606), -1):
    number = i
    new_op = equality_check.replace("humn", str(number))
    new_no_end = no_end.replace("humn", str(number))
    checkeq = eval(new_op)
    checnum = eval(new_no_end) 
    print(checkeq, checnum, number) 
'''
for number in range(3353687996500, 3353687996600, 1): 
    new_op = equality_check.replace("humn", str(number))
    new_no_end = no_end.replace("humn", str(number))
    checkeq = eval(new_op)
    checnum = eval(new_no_end)   
    if checkeq == True:
        print(number) 