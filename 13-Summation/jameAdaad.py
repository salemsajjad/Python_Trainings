string = input()
no_ones = 0
no_twos = 0
no_threes = 0

for adad in string:
    if adad == '1':
        no_ones += 1
    elif adad == '2':
        no_twos += 1
    elif adad == '3':
        no_threes += 1

string = "1+"*no_ones + "2+"*no_twos + "3+"*no_threes
string = string[:-1]
print(string)