import sys

num = int(input())

count = [0] * 10001

for i in range(num):
    input = int(sys.stdin.readline())
    
    count[input] += 1
    
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
