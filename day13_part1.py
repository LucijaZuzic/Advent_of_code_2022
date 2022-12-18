file = open("input_day13.txt", "r")
lines = file.readlines() 

def parse_array(line, lists): 
    while line.find("]") != -1:
        first_divide = len(line) - line[::-1].find("[")  
        last_divide = line[first_divide:].find("]") + first_divide
        values, lists = parse_array(line[first_divide:last_divide], lists)
        lists.append(values)
        line = line.replace(line[first_divide - 1:last_divide + 1], "s")
    numbers = line
    if line.find(",") != -1:
        numbers = line.split(",")
    list_num = len(lists) - 1
    return_values = []
    for i in range(len(numbers)):
        if numbers[i] == 's':
            return_values.append(lists[list_num])
            list_num -= 1
        else:
            return_values.append(int(numbers[i]))
    return return_values, lists

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")  
    old = lines[i]
    if lines[i] != '':
        #lines[i] = parse_array(lines[i], [])[0][0]
        lines[i] = eval(lines[i]) 
        
def compare_list(a, b):  
    for j in range(len(a)):
        if len(b) - 1 < j: 
            return -1
        if type(a[j]) == int:
            if type(b[j]) == int:
                if a[j] > b[j]: 
                    return -1
                if a[j] < b[j]:
                    return 1
            else:
                element_correct = compare_list([a[j]], b[j])
                if element_correct != 0:
                    return element_correct
        else:
            if type(b[j]) == int:
                element_correct = compare_list(a[j], [b[j]])
                if element_correct != 0:
                    return element_correct
            else:
                element_correct = compare_list(a[j], b[j])
                if element_correct != 0:
                    return element_correct
    if len(b) > len(a): 
        return 1
    return 0

index = 0
sum_correct = 0
for i in range(0, len(lines), 3): 
    index += 1
    if compare_list(lines[i], lines[i + 1]) == 1:
        sum_correct += index
print(sum_correct)
