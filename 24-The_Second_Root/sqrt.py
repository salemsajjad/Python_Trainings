from math import sqrt
tedad = int(input())
list = []
for i in range(0, tedad):
    list.append(int(sqrt(float(input()))*10000) / 10000)

for i in range(0, tedad):
    print("%0.4f" %(list[i]))

