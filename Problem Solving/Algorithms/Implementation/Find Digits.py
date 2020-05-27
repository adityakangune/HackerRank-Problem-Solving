'''
l = []
c = 0
n = int(input())
s = str(n)
for i in s:
    l.append(i)
#print(l)
for i in l:
    if(int(i) == 0):
        pass
    elif(n%int(i) == 0):
        c += 1
print(c)
'''
# Complete the findDigits function below.
def findDigits(n):
     l = []
     c = 0
     s = str(n)
     for i in s:
          l.append(i)
     # print(l)
     for i in l:
          if (int(i) == 0):
               pass
          elif (n % int(i) == 0):
               c += 1
     print(c)


t = int(input())

for t_itr in range(t):
     n = int(input())
     findDigits(n)