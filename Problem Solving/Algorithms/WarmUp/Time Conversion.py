s = input()
hh = int(s[0:2])
mm = int(s[3:5])
ss = int(s[6:8])
f = s[8:]
if f == "PM" and hh != 12:
    hh = hh + 12
elif f == "AM" and hh ==12:
    hh = 0
print('{:02}:{:02}:{:02}'.format(hh, mm, ss))