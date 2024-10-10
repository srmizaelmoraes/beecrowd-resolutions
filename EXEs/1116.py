n = int(input())
i = 1

while i <= n:
    
    i += 1
    x, y = map(int, input().split())
    
    if y == 0:
        print("divisao impossivel")
    else:
        div = x / y
        print("{:.1f}".format(div))