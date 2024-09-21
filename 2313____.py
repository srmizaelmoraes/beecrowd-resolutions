a, b, c = map(float, input().split())

if a >= (b + c):
    print("Invalido")

if a == b and b == c:
    print("Valido-Equilatero")
    
if a != b and b != c:
    print("Valido-Escaleno")
    
if (a == b and b != c) or (b == c and c != a):
    print("Valido-Isoceles")
    

    
if