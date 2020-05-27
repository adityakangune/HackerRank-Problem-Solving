CheckList = []
s = input()
s = s.lower()
l = ['a','s','f','d','g','h','j','k','l','p','o','i','u','y','t','r','e','w','q','z','x','c','v','b','n','m']
l.sort()
for i in s:
    CheckList.append(i)
#CheckList = set(CheckList)
#CheckList = list(CheckList)
for k in CheckList:
    if k == " ":
        #print("space")
        CheckList.remove(k)

CheckList = set(CheckList)
CheckList = list(CheckList)
CheckList.sort()
#print(CheckList)
if(CheckList == l):
   print("pangram")
else:
    print("not pangram")