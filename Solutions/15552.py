import sys

length = int(sys.stdin.readline())

for _ in range(length):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
