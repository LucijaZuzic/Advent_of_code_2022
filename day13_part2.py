file = open("input_day13.txt", "r")
lines = file.readlines() 

new_lines = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")  
    old = lines[i]
    if lines[i] != '': 
        new_lines.append(eval(lines[i]))
        
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

find1 = [[2]]
find2 = [[6]]
new_lines.append(find1)
new_lines.append(find2)
incorrect = True

while incorrect:
    incorrect = False
    for i in range(len(new_lines) - 1): 
        if compare_list(new_lines[i], new_lines[i + 1]) == -1: 
            backup = new_lines[i]
            new_lines[i] = new_lines[i + 1]
            new_lines[i + 1] = backup
            incorrect = True
            
result = 1
for i in range(len(new_lines)):
    if compare_list(new_lines[i], find1) == 0:
        result *= (i + 1)
    if compare_list(new_lines[i], find2) == 0:
        result *= (i + 1)
print(result)