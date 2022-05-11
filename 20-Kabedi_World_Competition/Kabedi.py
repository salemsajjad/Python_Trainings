tedad = int(input())
bazi = input()
list_bazi = bazi.split()
list_bazi = [int(x) for x in list_bazi]
count_below_3 = 0
for x in list_bazi:
    if x < 3:
       count_below_3 += 1

print(count_below_3 //3) 
