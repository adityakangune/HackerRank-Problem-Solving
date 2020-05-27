l = []
lr = []
dl = []
dlr = []
def FunnyString(s):

    for i in s:
        k1 = ord(i)
        l.append(k1)
    for j in r:
        k2 = ord(j)
        lr.append(k2)
#   print(l)
#   print(lr)
    for i in range(1 , len(l)):
        dl.append(abs(l[i] - l[i-1]))
#   print(dl)
    for i in range(1 , len(lr)):
        dlr.append(abs(lr[i] - lr[i-1]))
#    print(dlr)
    if dl == dlr:
        print("Funny")
    else:
        print("Not Funny")
    l.clear()
    lr.clear()
    dl.clear()
    dlr.clear()


q = int(input())
for i in range(q):
    s = input()
    r = s[::-1]
    FunnyString(s)





