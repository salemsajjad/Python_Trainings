def maghsoom(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count = count + 1
    return count

final_number = 0
max = 0
for i in range(1,21):
    adad = int(input())
    ma = maghsoom(adad)
    if ma > max:
        final_number = adad
        max = ma
    if ma == max:
        if adad > final_number:
            final_number = adad

print(final_number, max)


