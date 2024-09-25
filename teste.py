m = 0
i = 0
for i in range(7):
    n = float(input()) 
    if n > 0:
        i = i + 1
        m = m + n  
        media = m / i

print("{} valores positivos\n{:.1f}".format(i, media))