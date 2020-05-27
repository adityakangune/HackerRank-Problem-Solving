def count(s):

    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
    return c
n = int(input())
for _ in range(n):
    s = input()
    print(count(s))