from sys import stdin

def input():
    return stdin.readline().rstrip()

def gcd(a, b): 
    while b > 0:
        a, b = b, a % b
    return a

num = int(input())
arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    k = gcd(arr[0], arr[i])
    print(str(int(arr[0] / k)) + "/" + str(int(arr[i] / k)))
