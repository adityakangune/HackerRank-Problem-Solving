def median():
    if len(arr) % 2 != 0:
        print(arr[len(arr) // 2])
    elif len(arr) % 2 == 0:
        k = len(arr) // 2
        print((arr[k - 1] + arr[k]) / 2)


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    arr.sort()
    median()
