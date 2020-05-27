n = int(input())
factorial = 1
if(n == 1):
    print(factorial)
elif(n > 1):
    for i in range(2,n + 1):
        factorial = factorial * i
    print(factorial)
