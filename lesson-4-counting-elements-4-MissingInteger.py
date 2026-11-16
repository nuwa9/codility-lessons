import random

def missing_integer(A):
    N = len(A)
    B = [False] * (N + 1)
    for value in A:
        if 0 < value < N + 1:
            B[value] = True
    for index in range(1, N + 1):
        if not B[index]:
            return index
    return N + 1

input = [1, 3, 4, 5, 6, 7, 8]
random.shuffle(input)
print(missing_integer(input))