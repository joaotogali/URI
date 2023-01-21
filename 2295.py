
#Preço do alcool(entre 0.01 e 10.00)
#Preço do litro de gasolina(entre 0.01 e 10.00)
#preço do litro do alcool
#Preço da gasolina
#km p\litro que faz no alcool
#No caso de não haver difrença, dar prefencia a gasolina

#codigo
a, g, ra, rg = [float(x) for x in input().split()]
if (ra/a) <= (rg/g):
    print('G')
else:
    print('A')