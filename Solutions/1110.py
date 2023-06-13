import sys

num = int(sys.stdin.readline())
origin = num
cnt = 0

while True:
    if (num < 10):
        num = num * 10 + num
    else:
        num = (num % 10) * 10 + ((num // 10) + (num % 10)) % 10
    cnt += 1
    if (num == origin):
        break
print(cnt)
