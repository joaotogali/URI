#Ler o valor
valor = int(input())
#Imprime o valor
print(valor)
#Para cada celula, da maior para a menor calcule a qtd de cedulas
cedulas = [100, 50, 20, 10, 5, 2, 1]
for cedula in cedulas:
    qnt_cedulas = int(valor / cedula)
    print(f'{qnt_cedulas} nota(s) de R$ {cedula},00' )
    valor -= qnt_cedulas * cedula
