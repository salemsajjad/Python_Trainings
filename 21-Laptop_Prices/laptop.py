anbari = {}
tedad = int(input())
geymat = keifiat = 0
l_geymat=[]
l_keifiat = []
vaziat_parisa = 'poor irsa'
for i in range(0, tedad):
    s = input()
    geymat, keifiat = s.split()
    anbari[geymat] = keifiat
    l_geymat.append(int(geymat))
    l_keifiat.append(int(keifiat))

for i in range(0, tedad-1):
    if l_geymat[i+1]>l_geymat[i]:
        if l_keifiat[i]>l_keifiat[i+1]:
            vaziat_parisa = 'happy irsa'

print(vaziat_parisa)

#Soal Ebham Dare Vasam score = 60%