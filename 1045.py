a, b, c = map(float, input().split())

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif (a**2) == ((b**2) + (c**2)):
    print("TRIANGULO RETANGULO")
elif 