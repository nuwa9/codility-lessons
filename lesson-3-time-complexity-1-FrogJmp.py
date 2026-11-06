import math

def leap(X, Y, D):
    Z = Y - X
    N = math.floor(Z / D)
    return N if N * D >= Z else N + 1

print(leap(85, 86, 30))