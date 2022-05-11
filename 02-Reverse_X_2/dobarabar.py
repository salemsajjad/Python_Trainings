value = int(input())
makoos = 100*(value % 10) + 10*((value // 10)%10) + (value //100)
print(2*makoos)