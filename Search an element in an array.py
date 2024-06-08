def contains(n, x, a):
    if x in a:
        return "YES"
    else:
        return "NO"

n, x = map(int, input().split())
a = list(map(int, input().split()))

result = contains(n, x, a)
print(result)