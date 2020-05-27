l = []
l1 = []
bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

for i in range(len(keyboards)):
    for j in range(len(drives)):
        l.append(keyboards[i] + drives[j])
for i in l:
    if i < b:
        l1.append(i)
if l1 != []:
    print(max(l1))
else :
    print("-1")