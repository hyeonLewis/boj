from sys import stdin

def input():
    return stdin.readline().rstrip()

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a // b == a / b:
        print("multiple")
    elif b // a == b / a:
        print("factor")
    else:
        print("neither")
