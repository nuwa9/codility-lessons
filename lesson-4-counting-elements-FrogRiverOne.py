def frog_river_one(X, A):
    sieve = (X + 1) * [True]
    for K in range(len(A)):
        if sieve[A[K]]:
            X = X - 1
            if X == 0:
                return K
        sieve[A[K]] = False
    return -1

def gen_array(X):
    result = (X + 1) * [0]
    for i in range(X + 1):
        result[i] = i
    return result

print(frog_river_one(5000, gen_array(5000)))