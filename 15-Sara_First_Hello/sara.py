# chat = input()
# if ('h' in chat) and ('e' in chat) and ('ll' in chat) and ('o' in chat):
#     found = 1
# else :
#     found = 0

# if (found == 1):
#     h_pos = chat.find('h')
#     e_pos = chat.find('e')
#     ll_pos = chat.find('ll')
#     o_pos = chat.find('o')
#     if e_pos > h_pos and ll_pos > e_pos and o_pos > ll_pos :
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")

inpt=input()
h1=inpt.find('h')
h2=inpt.find('e',h1+1)
h3=inpt.find('l',h2+1)
h4=inpt.find('l',h3+1)
h5=inpt.find('o',h4+1)
TF=h1>=0 and h2>h1 and h3>h2 and h4>h3 and h5>h4
if TF:
    print('YES')
else:
    print('NO')            
    

    