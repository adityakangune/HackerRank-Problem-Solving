def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            l.append(0)
        else:
            l.append(1)
    for z in l:
        print(z, end = "")


l = []
s = input()
t = input()
strings_xor(s, t)



