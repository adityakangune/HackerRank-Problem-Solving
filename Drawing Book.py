n = int(input())
p =int(input())
totalSteps = n // 2
front = p // 2
back = totalSteps - front
print(min(front, back))