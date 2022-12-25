file = open("input_day20.txt", "r")
lines = file.readlines()  
list_num = [] 
previous = dict()
next = dict()

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    list_num.append(int(lines[i])) 

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

for i in range(len(list_num)): 
    for j in range(abs(list_num[i])): 
        if list_num[i] > 0:
            move_up(i)
        else:
            move_down(i) 
             
print(find_offset(0, 1000), find_offset(0, 2000), find_offset(0, 3000))
             
print(find_offset(0, 1000) + find_offset(0, 2000) + find_offset(0, 3000))