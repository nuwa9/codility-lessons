def tape_equilibrium(A):
    if len(A) <= 2:
        return abs(sum(A[:len(A) - 1]) - A[-1])
    B = A.copy()
    for i in range(1, len(A)):
        A[i] = A[i] + A[i - 1]
        B[len(A) - i - 1] = B[len(A) - i - 1] + B[len(A) - i]
    for i in range(1, len(A)):
        A[i - 1] = abs(A[i - 1] - B[i])
    return(min(A[:-1]))


print(tape_equilibrium([1,4,4,2,3,4,5,43,54,3,2,34,23]))