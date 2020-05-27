n = int(input())
l = []
arr = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j]:
            l.append(abs(i - j))
l = set(l)
l.remove(0)
try :
    print(min(l))
except:
    print(-1)

