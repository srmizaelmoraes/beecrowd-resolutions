salario = float(input())

if salario > 0 and salario <= 400:
    reajuste = salario * 0.15
    ns = salario + reajuste
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(ns, reajuste))

elif salario >= 400.01 and salario <= 800:
    reajuste = salario * 0.12
    ns = salario + reajuste
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(ns, reajuste))

elif salario >= 800.01 and salario <= 1200:
    reajuste = salario * 0.10
    ns = salario + reajuste
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(ns, reajuste))

elif salario >= 1200.01 and salario <= 2000:
    reajuste = salario * 0.07
    ns = salario + reajuste
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(ns, reajuste))

else:
    reajuste = salario * 0.04
    ns = salario + reajuste
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(ns, reajuste))