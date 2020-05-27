n = int(input())
people = 5
likes = 0
l = []
for i in range(n):
    likes = people // 2
    people = likes * 3
    l.append(likes)
print(sum(l))
