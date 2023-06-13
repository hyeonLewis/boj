n = input()
m = len(n)
start = int(n) - 9 * m
if start < 0:
    start = 0
for i in range(start, int(n) + 1):
    if (i + sum(map(int, str(i)))) == int(n):
        print(i)
        break
    if i == int(n):
        print(0)
