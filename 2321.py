#Ler os valores
j, o, a, u = map(int,input().split())
g, b, r, i = map(int,input().split())

#intersseções
int_x = not(a < g or j > r)
int_y = not(u < b or o > i)


#mostrar 0 caso não haja colisão e 1 caso não haja

if int_x and int_y:
    print(1)
else:
    print(0)
