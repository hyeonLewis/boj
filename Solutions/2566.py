import sys

arr = [[0 for col in range(9)] for row in range(9)]
for i in range(9):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    
candidate = -1;
row = -1;

for i in range(9):
    if (candidate < max(arr[i])):
        candidate = max(arr[i])
        row = i

print(candidate)
print(row + 1, arr[row].index(candidate) + 1)
