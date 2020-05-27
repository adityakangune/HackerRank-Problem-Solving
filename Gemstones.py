n = int(input())
rocks = []
for i in range(n):
    rocks.append(input())
#print(rocks)
i = set(rocks[0])
for j in range(1,n):
    i = i & set(rocks[j])
#print(i)
print(len(i))