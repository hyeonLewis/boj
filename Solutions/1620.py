from sys import stdin

def input():
    return stdin.readline().rstrip()

aToNum = {}
numToA = {}

n, m = map(int, input().split())

for i in range(n):
    name = input()
    aToNum[name] = i
    numToA[i] = name

for j in range(m):
    quiz = input()
    if quiz.isdigit():
        print(numToA[int(quiz)-1])
    else:
        print(aToNum[quiz]+1)
