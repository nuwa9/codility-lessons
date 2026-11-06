import math

def binary_gap(N):
    max = 0
    count = 0
    while N % 2 == 0:
        N = math.floor(N/2)
    while N > 0:
        if N % 2 == 1:
            max = max if max > count else count
            count = 0
        else:
            count = count + 1
        N = math.floor(N/2)
    return max

print(binary_gap(32))