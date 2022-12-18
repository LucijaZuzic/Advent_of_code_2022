class rock:  
    rocks = []  
    sorted_rocks = []   
    rocks_by_right = [dict() for i in range(0, 6)]
    rocks_by_left = [dict() for i in range(0, 6)]
    rocks_by_low = [dict() for i in range(0, 6)]
    rocks_by_high= [dict() for i in range(0, 6)]

    def addToDicts(self):
        if self.left not in rock.rocks_by_left[self.type_of_rock]:
            rock.rocks_by_left[self.type_of_rock][self.left] = [self]
        else:
            if self not in rock.rocks_by_left[self.type_of_rock][self.left]:
                rock.rocks_by_left[self.type_of_rock][self.left].append(self)

        if self.right not in rock.rocks_by_right[self.type_of_rock]:
            rock.rocks_by_right[self.type_of_rock][self.right] = [self]
        else:
            if self not in rock.rocks_by_right[self.type_of_rock][self.right]:
                rock.rocks_by_right[self.type_of_rock][self.right].append(self)

        if self.low not in rock.rocks_by_low[self.type_of_rock]:
            rock.rocks_by_low[self.type_of_rock][self.low] = [self]
        else:
            if self not in rock.rocks_by_low[self.type_of_rock][self.low]:
                rock.rocks_by_low[self.type_of_rock][self.low].append(self)

        if self.high not in rock.rocks_by_high[self.type_of_rock]:
            rock.rocks_by_high[self.type_of_rock][self.high] = [self]
        else:
            if self not in rock.rocks_by_high[self.type_of_rock][self.high]:
                rock.rocks_by_high[self.type_of_rock][self.high].append(self)  

    def removeFromDicts(self):
        if self.left in rock.rocks_by_left[self.type_of_rock]:
            if self in rock.rocks_by_left[self.type_of_rock][self.left]:
                rock.rocks_by_left[self.type_of_rock][self.left].remove(self)

        if self.right in rock.rocks_by_right[self.type_of_rock]:
            if self in rock.rocks_by_right[self.type_of_rock][self.right]:
                rock.rocks_by_right[self.type_of_rock][self.right].remove(self)

        if self.low in rock.rocks_by_low[self.type_of_rock]:
            if self in rock.rocks_by_low[self.type_of_rock][self.low]:
                rock.rocks_by_low[self.type_of_rock][self.low].remove(self)

        if self.high in rock.rocks_by_high[self.type_of_rock]:
            if self in rock.rocks_by_high[self.type_of_rock][self.high]:
                rock.rocks_by_high[self.type_of_rock][self.high].remove(self)  

    def getLast():
        return rock.rocks[-1]
    
    def getHighest():
        rock.sorted_rocks.sort(key=lambda x: x.high, reverse=True)
        return rock.sorted_rocks[0] 

    def __init__(self, type_of_rock, low = -1): 
        self.type_of_rock = type_of_rock
        self.low = low + 4
        self.left = 2
        self.id = len(rock.rocks)
        rock.rocks.append(self)
        rock.sorted_rocks.append(self)
        if self.type_of_rock == 1:
            self.right = self.left + 3
            self.high = self.low
        if self.type_of_rock == 2 or self.type_of_rock == 3:
            self.right = self.left + 2
            self.high = self.low + 2
        if self.type_of_rock == 4:
            self.right = self.left
            self.high = self.low + 3
        if self.type_of_rock == 5:
            self.right = self.left + 1
            self.high = self.low + 1 
        self.addToDicts()
        #print("Made", self.id, self.low, self.high, self.left, self.right)   

    def move_down(self): 
        if self.low > 0: 
            x_begin = self.left
            x_end = self.right 
            y_begin = self.low
            y_end = self.low
            if self.type_of_rock == 2:
                y_end += 1
            for x in range(x_begin, x_end + 1):
                for y in range(y_begin, y_end + 1):
                    if self.type_of_rock == 2 and y == self.low and x != self.left + 1:
                        continue
                    if self.type_of_rock == 2 and y != self.low and x == self.left + 1:
                        continue 
                    for other_type in range(1, 6):
                        min_high = y - 1
                        if other_type == 1:
                            max_high = y - 1
                        if other_type == 2 or other_type == 3:  
                            max_high = y + 1
                        if other_type == 4:  
                            max_high = y + 2
                        if other_type == 5:  
                            max_high = y
                        for other_high in range(min_high, max_high + 1):
                            if other_high not in rock.rocks_by_high[other_type]:
                                continue
                            for other_rock in rock.rocks_by_high[other_type][other_high]:
                                if other_rock is not self:
                                    if other_rock.covers_position(x, y - 1):  
                                        return False   
            self.removeFromDicts()
            self.low -= 1
            self.high -= 1
            self.addToDicts()
            return True
        else: 
            return False

    def move_right(self): 
        if self.right < 6:
            x_begin = self.right
            x_end = self.right 
            y_begin = self.low
            y_end = self.high
            if self.type_of_rock == 2:
                x_begin -= 1
            for x in range(x_begin, x_end + 1):
                for y in range(y_begin, y_end + 1):
                    if self.type_of_rock == 2 and y != self.low + 1 and x == self.right:
                        continue
                    if self.type_of_rock == 2 and y == self.low + 1 and x != self.right:
                        continue
                    for other_type in range(1, 6):
                        min_right = x + 1
                        if other_type == 1:
                            max_right = x + 4
                        if other_type == 2 or other_type == 3: 
                            max_right = x + 3
                        if other_type == 4:  
                            max_right = x + 1
                        if other_type == 5:  
                            max_right = x + 2
                        for other_right in range(min_right, max_right + 1):
                            if other_right not in rock.rocks_by_right[other_type]:
                                continue
                            for other_rock in rock.rocks_by_right[other_type][other_right]:
                                if other_rock is not self:
                                    if other_rock.covers_position(x + 1, y):  
                                        return   
            self.removeFromDicts()
            self.right += 1
            self.left += 1
            self.addToDicts()
            return 
        else:
            return

    def move_left(self): 
        if self.left > 0:
            x_begin = self.left
            x_end = self.left 
            y_begin = self.low
            y_end = self.high
            if self.type_of_rock == 2:
                x_end += 1
            if self.type_of_rock == 3:
                x_end = self.right
            for x in range(x_begin, x_end + 1):
                if self.type_of_rock == 3 and x == self.left + 1:
                    continue
                for y in range(y_begin, y_end + 1):
                    if self.type_of_rock == 3 and x == self.left and y != self.low:
                        continue
                    if self.type_of_rock == 3 and x == self.right and y == self.low:
                        continue
                    if self.type_of_rock == 2 and y != self.low + 1 and x == self.left:
                        continue
                    if self.type_of_rock == 2 and y == self.low + 1 and x != self.left:
                        continue
                    for other_type in range(1, 6):
                        min_right = x - 1
                        if other_type == 1:
                            max_right = x + 2
                        if other_type == 2 or other_type == 3: 
                            max_right = x + 1
                        if other_type == 4:  
                            max_right = x - 1
                        if other_type == 5:  
                            max_right = x 
                        for other_right in range(min_right, max_right + 1):
                            if other_right not in rock.rocks_by_right[other_type]:
                                continue
                            for other_rock in rock.rocks_by_right[other_type][other_right]:
                                if other_rock is not self:
                                    if other_rock.covers_position(x - 1, y):  
                                        return     
            self.removeFromDicts()
            self.right -= 1
            self.left -= 1
            self.addToDicts()
            return 
        else:
            return

    def covers_position(self, x, y):
        if self.type_of_rock == 1:
            if y == self.low:
                if x >= self.left and x <= self.right:
                    return True
                else:
                    return False
            else:
                return False

        if self.type_of_rock == 2:
            if y == self.low + 1:
                if x >= self.left and x <= self.right:
                    return True
                else:
                    return False
            else:
                if y == self.low:
                    if x == self.left + 1:
                        return True
                    else:
                        return False
                else: 
                    if y == self.high:
                        if x == self.left + 1:
                            return True
                        else:
                            return False
                    else:
                        return False

        if self.type_of_rock == 3:
            if y == self.low:
                if x >= self.left and x <= self.right:
                    return True
                else:
                    return False
            else:
                if x == self.right:
                    if y >= self.low and y <= self.high:
                        return True
                    else:
                        return False
                else:
                    return False
                
        if self.type_of_rock == 4:
            if x == self.left:
                if y >= self.low and y <= self.high:
                    return True
                else:
                    return False
            else:
                return False

        if self.type_of_rock == 5:
            if y >= self.low and y <= self.high and x >= self.left and x <= self.right:
                return True
            else:
                return False

file = open("input_day17.txt", "r")  
lines = file.readlines()   
map_one_row = ['.' for i in range(7)]
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "") 
line = lines[0] 

def addNewRock(): 
    if len(rock.rocks) != 0:
        highestRock = rock.getHighest()
        rock(len(rock.rocks) % 5 + 1, highestRock.high)
    else:
        rock(len(rock.rocks) % 5 + 1)

index = 0
addNewRock()
while len(rock.rocks) != 2025: 
    lastRock = rock.getLast()

    if line[index] == '<':
        lastRock.move_left()
    else:
        lastRock.move_right()  

    retval = lastRock.move_down()  
    if not retval:
        if len(rock.rocks) == 2022:
            break
        addNewRock()

    index += 1
    if index == len(line):
        index = 0

def print_tower():
    for y in range(rock.getHighest().high, -1, -1):
        print_str = ''
        for x in range(0, 7):
            char = '.'
            for some_rock in rock.rocks:
                if some_rock.covers_position(x, y):
                    char = '#'
                    break
            print_str += char
        print(print_str)
#print(line)
#print_tower()
print(rock.getHighest().high + 1)