def students():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    attendance = list(map(int, input().split()))
    late = []

    for i in attendance:
        if int(i) > 0:
            late.append(i)
    OnTime = n - len(late)

    if OnTime < k:
        print("YES")
    else:
        print("NO")


t = int(input())
for i in range(t):
    students()





