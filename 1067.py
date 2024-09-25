m = -1
p = -1
for i in range(1, 101):
    n = int(input())
    if n > m:
        m = n
        p = i       
print("{}\n{}".format(m, p))