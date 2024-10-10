from decimal import Decimal
n = Decimal(input())
centavos = int(n * 100)
nota100 = int(n // 100)
n %= 100
nota50 = int(n // 50)
n %= 50
nota20 = int(n // 20)
n %= 20
nota10 = int(n // 10)
n %= 10
nota5 = int(n // 5)
n %= 5
nota2 = int(n // 2)
n %= 2
nota1 = int(n // 1)
centavos = int(centavos % 100)
moeda50 = int(centavos // 50)
centavos %= 50
moeda25 = int(centavos // 25)
centavos %= 25
moeda10 = int(centavos // 10)
centavos %= 10
moeda5 = int(centavos // 5)
centavos %= 5
moeda1 = int(centavos)
print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{nota1} moeda(s) de R$ 1.00")
print(f"{moeda50} moeda(s) de R$ 0.50")
print(f"{moeda25} moeda(s) de R$ 0.25")
print(f"{moeda10} moeda(s) de R$ 0.10")
print(f"{moeda5} moeda(s) de R$ 0.05")
print(f"{moeda1} moeda(s) de R$ 0.01")
