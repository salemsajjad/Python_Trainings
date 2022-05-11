def reverse(string):
    string = string.lower()
    reverse = string[::-1]
    return reverse

s = input()
output = reverse(s)
if output == s.lower() :
    print("palindrome")
else:
    print("not palindrome")
