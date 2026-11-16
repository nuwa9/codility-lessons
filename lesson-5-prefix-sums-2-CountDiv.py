import math

def count_div(A, B, K):
    if A > 0:
        return math.floor(B / K) - math.floor((A - 1) / K) if B >= K else 0
    else:
        return math.floor(B / K) + 1

print(count_div(6, 11, 2))