c = 0
n = int(input())
socks = list(map(int, input().rstrip().split()))
colours = set(socks)
for i in colours:
    c = c + socks.count(i) // 2
print(c)

