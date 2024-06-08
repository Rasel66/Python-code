t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    originalCost = sum(a);
    newCost = 0;
    for i in a:
        if i >= y:
            newCost += (i - y)
    newCost += x

    if newCost < originalCost:
        print("COUPON")
    else:
        print("NO COUPON")