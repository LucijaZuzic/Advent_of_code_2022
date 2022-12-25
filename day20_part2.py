file = open("input_day20.txt", "r")
lines = file.readlines()  
list_num = [] 
previous = dict()
next = dict()
mul = 811589153
round = 10

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    list_num.append(int(lines[i]) * mul) 

for i in range(len(list_num)):
    if i != len(list_num) - 1:
        next[i] = i + 1
    if i != 0:
        previous[i] = i - 1
next[len(list_num) - 1] = 0
previous[0] = len(list_num) - 1

def move_up(number):
    old_next = next[number]
    old_previous = previous[number]
    next[number] = next[old_next]
    previous[next[old_next]] = number
    next[old_next] = number
    previous[number] = old_next
    next[old_previous] = old_next 
    previous[old_next] = old_previous

def move_down(number):
    old_next = next[number]
    old_previous = previous[number]
    previous[number] = previous[old_previous] 
    next[previous[old_previous]] = number
    previous[old_previous] = number
    next[number] = old_previous
    previous[old_next] = old_previous 
    next[old_previous] = old_next 

def remove_num(number):
    old_next = next[number]
    old_previous = previous[number]
    next[old_previous] = old_next
    previous[old_next] = old_previous

def insert_after(number, old_number):
    old_next = next[number] 
    next[number] = old_number
    previous[old_number] = number
    next[old_number] = old_next
    previous[old_next] = old_number

def insert_before(number, old_number):
    old_previous = previous[number] 
    previous[number] = old_number
    next[old_number] = number 
    previous[old_number] = old_previous
    next[old_previous] = old_number

def insert_num(number): 
    if list_num[number] == 0:
        return
    offset = abs(list_num[number])
    offset %= len(list_num) - 1
    old_num = number 
    for i in range(offset):
        if list_num[old_num] > 0:
            number = next[number]
        else:
            number = previous[number]
    remove_num(old_num)
    if list_num[old_num] > 0: 
        insert_after(number, old_num)
    else: 
        insert_before(number, old_num)

def print_list(current, visited, string_print): 
    if current not in visited:
        string_print += " " + str(list_num[current])
        visited.add(current)
        return print_list(next[current], visited, string_print)
    else:
        return string_print

def find_offset(number, offset):
    offset %= len(list_num) 
    number = list_num.index(number)
    for i in range(offset):
        number = next[number]
    return list_num[number]

for k in range(round):
    for i in range(len(list_num)): 
        insert_num(i)
        
print(find_offset(0, 1000) + find_offset(0, 2000) + find_offset(0, 3000))