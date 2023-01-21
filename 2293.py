#Definir numero de linhas e colunas
escolha = [int(x) for x in str(input()).split()]

n = escolha[0]
m = escolha[1]
#criar a matriz
c = []
#Adicionar valores a matriz
for i in range(n):
    c.append([int(x) for x in str(input()).split()])
#Restrições para somar
for i in range(n):
    soma = 0
    for j in range(m):
        soma += c[i][j]
    if i == 0:
        k = soma
    elif soma > k:
        k = soma
for j in range(m):
    soma = 0
    for i in range(n):
        soma += c[i][j]
    if soma > k:
        k = soma
#Mostrar a soma da matriz
print(k)