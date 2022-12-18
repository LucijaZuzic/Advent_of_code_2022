file = open("input_day7.txt", "r")
directory_parents = {}
directory_children = {}
directory_sizes_immediate = {}
directory_sizes_total = {}
depth = {}
maxdepth = 0
current_dir = ''
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    if lines[i][0] == '$':
        if lines[i][2] == 'c':
            if lines[i][5] == '/':
                current_dir = '/'
                directory_parents[current_dir] = '' 
                depth[current_dir] = 0
                if current_dir not in directory_children:
                    directory_children[current_dir] = []
                if current_dir not in directory_sizes_immediate:
                    directory_sizes_immediate[current_dir] = set() 
                if current_dir not in directory_sizes_total:
                    directory_sizes_total[current_dir] = set() 
            else:
                if lines[i][5] == '.':
                    current_dir = directory_parents[current_dir]
                else:
                    new_dir = lines[i][5:]
                    if new_dir in directory_parents:
                        print("double")
                        new_dir = new_dir + " "
                    directory_parents[new_dir] = current_dir 
                    depth[new_dir] = depth[current_dir] + 1
                    maxdepth = max(depth[new_dir], maxdepth)
                    if new_dir not in directory_children:
                        directory_children[new_dir] = []
                    if new_dir not in directory_sizes_immediate:
                        directory_sizes_immediate[new_dir] = set() 
                    if new_dir not in directory_sizes_total:
                        directory_sizes_total[new_dir] = set() 
                    children = directory_children[current_dir]
                    if new_dir not in children:
                        children.append(new_dir)
                    directory_children[current_dir] = children
                    current_dir = new_dir
    else:
        if lines[i][0] == 'd':
            '''
            new_dir = lines[i][4:]
            if new_dir in directory_parents:
                print("double")
                new_dir = new_dir + " "
            directory_parents[new_dir] = current_dir 
            depth[new_dir] = depth[current_dir] + 1
            maxdepth = max(depth[new_dir], maxdepth)
            if new_dir not in directory_children:
                directory_children[new_dir] = []
            if new_dir not in directory_sizes_immediate:
                directory_sizes_immediate[new_dir] = set() 
            if new_dir not in directory_sizes_total:
                directory_sizes_total[new_dir] = set() 
            children = directory_children[current_dir]
            if new_dir not in children:
                children.append(new_dir)
            directory_children[current_dir] = children
            '''
        else:
            size_and_name = lines[i].split(" ")
            size_and_name[0] = int(size_and_name[0])
            directory_sizes_immediate[current_dir].add((size_and_name[0], size_and_name[1])) 
            directory_sizes_total[current_dir].add((size_and_name[0], size_and_name[1])) 
            parent = directory_parents[current_dir]
        
queue_dirs = []
visited = {}
print(maxdepth, len(depth))

depth_sorted = sorted(depth.items(), key=lambda x:x[1], reverse=True)
#print(depth_sorted)

for directory in depth_sorted:
    parent = directory_parents[directory[0]]
    if parent != '':  
        directory_sizes_total[parent] = directory_sizes_total[parent] | directory_sizes_total[directory[0]]
 
total_size = 0
for directory in directory_sizes_total:
    sizes = [file[0] for file in directory_sizes_total[directory]] 
    total = sum(sizes)
    if total <= 100000:
        total_size += total 
print(total_size)