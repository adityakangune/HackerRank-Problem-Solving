n = int(input())
ar = list(map(int, input().split()))
dict = {}
for i in ar:
    dict[ar.count(i)] = i
most = max(dict.keys())
element = dict[most]
c = 0
for i in ar:
    if i != element:
        c += 1
print(c)
