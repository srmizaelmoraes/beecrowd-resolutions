c = float(input("Valor da conta: R$ "))
p = int(input("Quantida de pessoas: "))

calc = c / p

if calc > 50:
    print("Conta alta")
else:
    print("Conta dentro deo esperado!")