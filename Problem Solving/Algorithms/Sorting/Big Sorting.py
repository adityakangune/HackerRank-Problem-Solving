unsorted = []
n = int(input())
for i in range(n):
    c = int(input())
    unsorted.append(c)
unsorted.sort()
for i in unsorted:
    print(i)