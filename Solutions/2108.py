import sys

num = int(sys.stdin.readline())
arr = [0] * num
count = [0] * 8001
for i in range(num):
    arr[i] = int(sys.stdin.readline())
    count[4000 + arr[i]] += 1

print(round(sum(arr) / num))
freq = max(count)
if (count.count(freq) > 1):
    freq = count.index(freq, count.index(freq) + 1) - 4000
else:
    freq = count.index(freq) - 4000
arr.sort()
print(arr[int(len(arr) / 2)])
print(freq)
print(max(arr) - min(arr))
