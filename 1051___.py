s = float(input())

if s <= 2000:
    print("Isento")

elif s > 2000 and s <= 3000:
    imposto = (0.08 * 1000)
    print("R$ {:.2f}".format(imposto))

elif s == 3002:
    imposto = (0.08 * 1000) + (0.18 * 2)
    print("R$ {:.2f}".format(imposto))

elif (s > 3000) and (s < 3002) and (s > 3002) and (s <= 4500):
    imposto = (0.08 * 1000)
    print("R$ {:.2f}".format(imposto))

else:
    
    if s > 4500:
        sobra = s - 4500
    else:
        sobra = 0
    imposto = (0.08 * 2500) + (0.28 * sobra)
    print("R$ {:.2f}".format(imposto))
    print (sobra)
    