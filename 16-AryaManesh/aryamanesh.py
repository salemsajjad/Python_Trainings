name = input()
lower = name.lower()

upper_count = 0
lower_count = 0
for i in range(0, len(name)):
    if name[i] < lower[i]:
        upper_count += 1
    else:
        lower_count += 1

if upper_count > lower_count:
    output = name.upper()
else:
    output = name.lower()

print(output)