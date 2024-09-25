i = 0
v = int(input())
iN = 0
out = 0
while i <= (v - 1):
    i += 1
    n = int(input())
    if n >= 10 and n <= 20:
        iN += 1
    else:
        out += 1
print("{} in\n{} out".format(iN, out))