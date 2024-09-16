valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
d = int(valores[3])
sunCD = c + d
sunAB = a + b
if (b > c and d > a and sunCD > sunAB and c > 0 and d > 0 and a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos") 