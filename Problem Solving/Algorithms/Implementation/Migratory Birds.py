n = int(input())
birds = list(map(int, input().rstrip().split()))
counts = [0]*n  # [0,0,0]
for i in birds:
    counts[i] += 1

#print(birds)
#print(counts)
print(counts.index(max(counts)))