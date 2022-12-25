file = open("input_day25.txt", "r")
lines = file.readlines()     

def snafudec(snafu):
    deci = 0
    pot = 1
    for i in range(len(snafu) - 1, -1, -1):
        c = snafu[i]
        if c == '1':
            deci += pot
        if c == '2':
            deci += pot * 2
        if c == '-':
            deci -= pot
        if c == '=':
            deci -= pot * 2
        pot *= 5
    return deci  

def dectosnafu(deci):
    pot = 0
    while pow(5, pot) < deci:
        pot += 1
    for i in range(pot):
        deci += 2 * pow(5, i)
    retval = ""
    while deci != 0:
        adddigi = deci % 5
        deci = int((deci - adddigi) / 5)
        if adddigi > 1:
            retval = str(adddigi - 2) + retval
        if adddigi == 1:
            retval = '-' + retval
        if adddigi == 0:
            retval = '=' + retval
    return retval

suma = 0
for i in range(len(lines)): 
    lines[i] = lines[i].replace("\n", "") 
    d = snafudec(lines[i])
    suma += d
print(dectosnafu(suma))