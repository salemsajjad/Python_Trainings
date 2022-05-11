first_mosen = 10
second_mosen = 10

sen = int(input())

while sen != -1:
    if sen > first_mosen:
        second_mosen = first_mosen
        first_mosen = sen
    elif sen <= first_mosen and sen > second_mosen:
        second_mosen = sen
    sen = int(input())

print(first_mosen, second_mosen)