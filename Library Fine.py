d1M1Y1 = input().split()

d1 = int(d1M1Y1[0])

m1 = int(d1M1Y1[1])

y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()

d2 = int(d2M2Y2[0])

m2 = int(d2M2Y2[1])

y2 = int(d2M2Y2[2])

if y1 > y2:
    fine = 10000
elif y1 == y2 and m1 > m2:
    fine = (m1 - m2) * 500
elif y1 == y2 and m1 == m2 and d1 > d2:
    fine = (d1 - d2) * 15
else:
    fine = 0

print(fine)