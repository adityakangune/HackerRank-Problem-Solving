input()
c = 0
l = []
arr = list(map(int, input().split()))
d, m = (input().split())
d = int(d)
m = int(m)
for i in range(m):
    if sum(l) <= d:
        l.append(i)
        c += 1
    sum(l) 

print(c)