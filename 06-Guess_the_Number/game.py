import random

a = 1
b = 99
javab = random.randint(a, b)
print("My answre is: ", javab)
idea = input("Please give me your idea: ")

while idea !='d':
    if idea =='k':
        b = javab -1
        javab = random.randint(a, b)
    
    elif idea =='b':
        a = javab +1
        javab = random.randint(a, b)

    print("My answre is: ", javab)
    idea = input("Please give me your idea: ")

print("OMG! winner winner chicken dinner! ")
