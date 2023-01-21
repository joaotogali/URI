#Ler um valor N que indica o numero de quantidades de casos
n = int(input())
for i in range(n):


    #Cada teste consiste em valores A e B onde tem que ser maior que 1 e até 1000 digitos
    a, b = list(map(str,input().split()))
    #Mostrar se o valor B se encaixa no valor A
    if a[-len(b):] == b:
        print( "encaixa")
    else:
        print("não encaixa")