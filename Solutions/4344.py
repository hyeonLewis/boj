import sys

num = int(sys.stdin.readline())

for _ in range(num):
    arr = list(map(int, sys.stdin.readline().split()))
    avg = sum(arr[1:]) / arr[0]
    cnt = 0
    for i in arr[1:]:
        if i > avg:
            cnt += 1
    print("%.3f%%" % round(cnt / arr[0] * 100, 3))
