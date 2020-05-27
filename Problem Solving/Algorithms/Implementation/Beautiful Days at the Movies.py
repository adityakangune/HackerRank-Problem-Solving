ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

z = 0
for c in range(i,j + 1):
    c = str(c)
    rev = c[::-1]
    c = int(c)
    rev = int(rev)
    if (rev - c) % k == 0:
        z += 1
print(z)
