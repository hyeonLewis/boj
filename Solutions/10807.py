import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

print(arr.count(target))
