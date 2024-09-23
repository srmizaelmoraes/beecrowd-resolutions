n1, n2, n3 = map(int, input().split())
numeros = [n1, n2, n3]
numeros.sort()
print(*numeros, sep='\n')
print(f"\n{n1}\n{n2}\n{n3}")