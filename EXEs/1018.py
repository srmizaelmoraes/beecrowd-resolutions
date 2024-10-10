valor = int(input())
print(valor)

print(valor // 100, "nota(s) de R$ 100,00")
div = valor % 100

print(div // 50, "nota(s) de R$ 50,00")
div = div % 50

print(div // 20, "nota(s) de R$ 20,00")
div = div % 20

print(div // 10, "nota(s) de R$ 10,00")
div = div % 10

print(div // 5, "nota(s) de R$ 5,00")
div = div % 5

print(div // 2, "nota(s) de R$ 2,00")
div = div % 2

print(div // 1, "nota(s) de R$ 1,00")