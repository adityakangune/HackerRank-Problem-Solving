s = input()
l = []
a = 0
b = 3
c = 0
for i in range(len(s) // 3):
    l.append(s[a:b])
    a += 3
    b += 3
for j in l:
    j = list(j)
    if j[0] != "S":
        c += 1
    if j[1] != "O":
        c += 1
    if j[2] != "S":
        c += 1
print(c)