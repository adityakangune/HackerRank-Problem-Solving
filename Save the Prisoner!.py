def prisoner():
    r = m % n
    if (r + s - 1) % n == 0:
        return n
    else:
        return (r + s - 1) % n




t =int(input())
for _ in range(t):
    nms = input().split()
    n = int(nms[0])
    m = int(nms[1])
    s = int(nms[2])
    print(prisoner())