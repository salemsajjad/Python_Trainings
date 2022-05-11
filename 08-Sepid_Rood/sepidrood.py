win = 0
draw = 0
lost = 0
sum = 0

for i in range(1,31):
    point = int(input())
    if point ==3:
        win = win + 1
        sum = sum + 3
    elif point ==1:
        draw = draw + 1
        sum = sum + 1
    elif point ==0:
        lost = lost + 1

print(sum , win)

