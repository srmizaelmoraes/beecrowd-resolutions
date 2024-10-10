line = input().split()
A = int(line[0])
B = int(line[1])
C = int(line[2])

if A >= B and A >= C:
    print('{} eh o maior'.format(A))

elif  B >= A and B >= C:
    print('{} eh o maior'.format(B))

else:
    print('{} eh o maior'.format(C))