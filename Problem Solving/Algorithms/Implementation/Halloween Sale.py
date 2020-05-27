pdms = input().split()
p = int(pdms[0])
d = int(pdms[1])
m = int(pdms[2])
s = int(pdms[3])

cost = p
l = []
while sum(l) <= s:
    if cost > m:
        l.append(cost)
        cost = cost - d
    if cost <= m:
        l.append(m)
print(len(l) - 1)