string = input()
count = 0 
string = string.lower()

for harf in string:
    if harf in ['a','o','e','i','u']:
        string = string.replace(harf,"")
final = ""

for i in range(0,len(string)):
    if string[i] != ' ':
        final += '.' + string[i]
    else:
        final += string[i]

print(final)