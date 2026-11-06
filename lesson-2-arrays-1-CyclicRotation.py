def rotate(A, K):
    for _ in range(K):
        last = A[len(A) - 1]
        for index in range(len(A) - 1, 0, -1):
            A[index] = A[index - 1]
        A[0] = last
    return A

def rotate_pop(A, K):
    if len(A) > 0:
        for _ in range(K):
            A.insert(0, A.pop())
    return A


print(rotate_pop([0, 1, 2, 3, 4, 5, 6], 1))