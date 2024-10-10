n = int(input())
ln = [n]

for i in range(9):
    ln[i] = i*2
for i in range(10):
    print(f"N{i} = {ln[i]}")