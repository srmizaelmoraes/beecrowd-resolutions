s = int(input())

h = int(s / 3600)
s = s - (h * 3600)
m = int(s / 60)
s = s - (m * 60)

print('{}:{}:{}'.format(h, m, s))