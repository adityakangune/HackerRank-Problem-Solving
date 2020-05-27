n = int(input())
sticks = list(map(int, input().rstrip().split()))
while len(sticks):
    print(len(sticks))
    sticks = [ j - min(sticks) for j in sticks]
    c = min(sticks)
    for k in range(sticks.count(c)):
        sticks.remove(c)

