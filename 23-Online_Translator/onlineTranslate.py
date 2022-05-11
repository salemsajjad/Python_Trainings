tedad = int(input())

words = dict()
list = []
for i in range(0, tedad):
    list = input().split()
    words[list[0]] = list[1]
    del list

# string = "we say goodbye to you tonight"
# sentence = string.split()
translate = []
sentence = input().split()
for word in sentence:
    if word in words.keys():
        translate.append(words[word])
    else:
        translate.append(word)

output = ' '.join(translate)
print(output)    