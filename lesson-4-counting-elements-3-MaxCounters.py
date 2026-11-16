def max_counters(N, A):
    counters = N * [0]
    max_value = 0
    maximized = False
    for K in A:
        if K > N:
            if not maximized:
                counters = N * [max_value]
                maximized = True
            continue
        maximized = False
        counters[K - 1] += 1
        if max_value < counters[K - 1]:
            max_value = counters[K - 1]
    return counters

print(max_counters(5, [3, 4, 4, 6, 1, 4, 4]))

# 77%