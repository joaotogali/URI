
t = 1
while True:
    n = int(input())#Ler numero de participantes
    if n == 0:
        break
    #Sequencia em ordem de entrada dos ingressos
    pessoas = [int(x) for x in input().split()]
    ganhador = [pessoas[x] for x in range(n) if pessoas[x] == (x+1)]

    print(f'Teste {t}')
    t += 1
    #Mostrar o ingresso do ganhador
    print(ganhador[0])
    print()