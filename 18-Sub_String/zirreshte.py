reshte = input()

if "AB" in reshte:
    reshte = reshte.replace("AB","@",1)
    if "BA" in reshte:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

# score 93%
# dar voroodi BABAB moshkel Dare!