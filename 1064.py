p = 0
m = 0
for i in range(6):
    n = float(input())
    if n > 0:
        p += 1
        m = m + n
print(f"{p} valores positivos\n {m/p:.1f}")