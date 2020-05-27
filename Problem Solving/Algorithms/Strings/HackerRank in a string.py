def check(s):
    l = []
    check = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    check = set(check)
    check = list(check)
    check.sort()
    # print(check)
    for i in s:
        if i == "h":
            l.append(i)
        elif i == "a":
            l.append(i)
        elif i == "c":
            l.append(i)
        elif i == "k":
            l.append(i)
        elif i == "e":
            l.append(i)
        elif i == "r":
            l.append(i)
        elif i == "n":
            l.append(i)
        elif i == "k":
            l.append(i)
    l = set(l)
    l = list(l)
    l.sort()
    # print(l)
    if l == check:
        print("YES")
    else:
        print("NO")





q = int(input())
for i in range(q):
    s = input()
    check(s)