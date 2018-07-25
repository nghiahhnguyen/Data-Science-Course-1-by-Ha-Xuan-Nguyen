M = [[1, 2, 3, 4, 5],
     [3, 4, 2, 5, 6],
     [1, 6, 3, 2, 5]]
m = len(M)
n = len(M[0])
l = []
for i in range(n):
    cnt = 0
    for j in range(m):
        cnt += M[j][i]
    l.append(cnt)
print(l)
