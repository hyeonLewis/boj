from sys import stdin

def input():
    return stdin.readline().rstrip()

case = int(input())

def solve(arr):
    center_distance = (abs(arr[0] - arr[3])**2 + abs(arr[1] - arr[4])**2)**0.5
    diameter = arr[2] + arr[5]
    if center_distance == diameter:
        return "1"
    elif center_distance > diameter:
        return "0"
    else:
        if center_distance + min(arr[2], arr[5]) < max(arr[2], arr[5]):
            return "0"
        elif center_distance + min(arr[2], arr[5]) == max(arr[2], arr[5]):
            return "1"
        else:
            return "2"

for _ in range(case):
    arr = list(map(int, input().split()))
    if arr[0] == arr[3] and arr[1] == arr[4]:
        if arr[2] != arr[5]:
            print("0")
        else:
            print("-1")
    else:
        result = solve(arr)
        print(result)
