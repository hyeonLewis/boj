import sys

arr = [i for i in range(1, 31)]

for _ in range(28):
    input = int(sys.stdin.readline())
    arr.remove(input)

print(min(arr))
print(max(arr))
