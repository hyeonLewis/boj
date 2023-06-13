a, b = map(int, input().split())

mapArr = [True] * (b + 1)

k = int(b**0.5)

for i in range(2, k + 1):
    if mapArr[i]:
        for j in range(i + i, b + 1, i):
            mapArr[j] = False
            
result = [i for i in range (a, b + 1) if mapArr[i]]
    
for i in result:
    if i != 1:
        print(i)
