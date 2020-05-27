import math

def f():
    l = []
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    sqa = math.ceil(math.sqrt(a))
    sqb = math.floor(math.sqrt(b))
    for i in range(sqa, sqb + 1):
        l.append(i)
    print(len(l))


t = int(input())
for i in range(t):
    f()
