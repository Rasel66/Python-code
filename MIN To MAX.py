def findMax(n, a):
    m = min(a)
    count = sum(1 for x in a if x!=m)
    return count

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = findMax(n, a)
    print(ans)