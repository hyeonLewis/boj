import sys

num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()
for i in arr:
    print(i)
