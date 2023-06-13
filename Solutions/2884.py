A, B = map(int, input().split())

Offset = 45

if B - Offset < 0:
    B = 60 + B - Offset
    if (A == 0):
        A = 23
    else:
        A -= 1
else:
    B -= Offset
    
print(A, B)
