n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))    
arr.sort()

def solve(arr, k):
    d = [10001] * (k + 1)
    d[0] = 0
    for i in range(n):
        for j in range(arr[i], k + 1):
            if d[j - arr[i]] != 10001:
                d[j] = min(d[j], d[j - arr[i]] + 1)
    if d[k] == 10001:
        return -1
    return d[k]

print(solve(arr, k))