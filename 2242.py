
risada = input()
vogais = ""
for r in risada:
    if (r=='a' or r=='e' or r=='i' or r=='o' or r=='u'):
        vogais +=r
if(vogais ==vogais[::-1]):
        print("S")
else:
        print("N")