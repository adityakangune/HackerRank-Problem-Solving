l = []
s = input()
n = int(input())
z = 0
for i in range(n):
    l.append(s[z])
    z += 1
    if z == len(s):
        z = 0
print(l.count("a"))
#print(l)