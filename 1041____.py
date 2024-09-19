#Para calcular a média ponderada, é preciso seguir os seguintes passos:
#Multiplicar cada informação pela sua respectiva ponderação;
#Somar os resultados das multiplicações;
#Dividir o resultado pela soma dos pesos. 

n1, n2, n3, n4 = map(float, input().split())
m2, m3, m4, m1 = 2, 3, 4, 1
media = ((n1 * m2) + (n2 * m3) + (n3 * m4) + (n4 * m1)) / (m2 + m3 + m4 + m1)
print("Media: {:.1f}".format(media))
if media 