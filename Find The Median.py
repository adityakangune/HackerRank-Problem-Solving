n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
k = len(arr) // 2
print(arr[k])