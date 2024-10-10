s = float(input())
if s <= 2000:
    print("Isento")
elif s > 2000 and s <= 3000:
    sobra = s - 2000
    imposto = (0.08 * sobra)
    print("R$ {:.2f}".format(imposto))
elif s > 3000 and s <= 4500:
    sobra = s - 3000
    imposto = (0.08 * 1000) + (0.18 * sobra)
    print("R$ {:.2f}".format(imposto))
else:
    sobra = s - 4500
    imposto = (0.08 * 1000) + (0.18 * 1500) + (0.28 * sobra)
    print("R$ {:.2f}".format(imposto))