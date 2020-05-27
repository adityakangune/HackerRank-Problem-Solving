def utopiantree():
    height = 1
    n = int(input())
    for i in range(1,n+1):
        if i % 2 != 0:
            height = height *2
        else:
            height += 1
    print(height)

testcases = int(input())
for _ in range(testcases):
    utopiantree()