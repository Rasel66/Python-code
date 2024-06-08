def solve(test_cases):
    max_steps = 60 
    precomputed = []

    for step in range(max_steps + 1):
        a = list(range(step + 1))
        for _ in range(step):
            new_a = a.copy()
            for i in range(1, len(a)):
                new_a[i] = a[i-1] | a[i] | (a[i+1] if i+1 < len(a) else 0)
            new_a[0] = a[0] | a[1]
            a = new_a
        precomputed.append(a)

    results = []
    for n, m in test_cases:
        if m <= max_steps:
            results.append(precomputed[m][n])
        else:
            results.append(precomputed[max_steps][n])

    return results

import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    test_cases.append((n, m))
    index += 2


results = solve(test_cases)
for result in results:
    print(result)
