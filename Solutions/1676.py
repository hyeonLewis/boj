from sys import stdin

def input():
    return stdin.readline().rstrip()

num = int(input())
a = num // 5
b = num // 25
c = num // 125
print(a + b + c)
