def standardize(name):
    name = name.lower()
    first = name[0].upper()
    last = name[1:]
    return first + last

standard =[]
for i in range(0,10):
    name = standardize(input())
    standard.append(name)

for i in range(0,10):   
    print (standard[i])