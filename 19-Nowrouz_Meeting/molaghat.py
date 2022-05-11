# manzel = input()
# list = manzel.split()
# list = [int(x) for x in list] 
# average = sum(list) / len(list)
# distance = int(abs(list[0] - average) + abs(list[1] - average) + abs(list[2] - average))
# print(distance)

manzel = input()
x1, x2, x3 = manzel.split()
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

print(max(x1, x2, x3) - min(x1, x2, x3))


