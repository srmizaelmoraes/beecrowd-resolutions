numbers = list(map(float, input().split()))

numbers.sort(reverse = True)

a = numbers[0]
b = numbers[1]
c = numbers[2]

if (a >= (b + c)):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")  
    elif (a**2) > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")   
    else:
        print("TRIANGULO ACUTANGULO") 
if a == b and b == c:
    print("TRIANGULO EQUILATERO")    
elif (a == b and b != c) or (b == c and c != a) or (c == a and c != b):
    print("TRIANGULO ISOSCELES")