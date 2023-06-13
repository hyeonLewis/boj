n, m = map(int, input().split())
arr = list(map(int, input().split()))
candidate = -1;
for i in range(n-2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if m - candidate > m - (arr[i] + arr[j] + arr[k]) and arr[i] + arr[j] + arr[k] <= m:
                candidate = arr[i] + arr[j] + arr[k]
            if candidate == m:
                break
print(candidate)
