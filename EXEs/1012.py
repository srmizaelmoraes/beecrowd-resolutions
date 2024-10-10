line = input().split()
A = float(line[0])
B = float(line[1])
C = float(line[2])
a = (A * C) / 2
b = (3.14159 * (C ** 2))
c = ((A + B) * C)/2
d = B ** 2
e = A * B
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(a, b, c, d, e))