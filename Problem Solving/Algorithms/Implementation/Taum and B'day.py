def CostGifts():
    if bc > wc + z:
        cost = (b + w) * wc + (z * b)
    elif wc > bc + z:
        cost = (b + w) * bc + (z * w)
    else:
        cost = (b * bc) + (w * wc)
    print(cost)





t = int(input())
for i in range(t):
    first_multiple_input = input().rstrip().split()
    b = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    bc = int(second_multiple_input[0])

    wc = int(second_multiple_input[1])

    z = int(second_multiple_input[2])

    CostGifts()
