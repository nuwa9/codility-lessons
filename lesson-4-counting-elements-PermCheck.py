def perm_check(A):
    if sum(A) != (len(A) * len(A) + len(A)) / 2:
        return 0
    sieve = (len(A) + 1) * [False]
    for N in A:
        if N > len(A) or sieve[N]:
            return 0
        sieve[N] = True
    for K in range(1, len(A) + 1):
        if not sieve[K]:
            return 0
    return 1

print(perm_check([1, 3, 4, 5, 6, 7, 8]))

print(perm_check([1, 2, 3, 4, 5, 6, 7, 8]))