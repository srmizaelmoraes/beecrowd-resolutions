line1 = input().split()
line2 = input().split()
x1 = float(line1[0])
y1 = float(line1[1])
x2 = float(line2[0])
y2 = float(line2[1])
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('{:.4f}'.format(distancia))