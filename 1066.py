par = 0
impar = 0
positivo = 0
negativo = 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    if n % 2 == 1:
        impar += 1
    if n > 0:
        positivo += 1 
    if n < 0:
        negativo += 1
print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivo} valor(es) positivo(s)\n{negativo} valor(es) negativo(s)")