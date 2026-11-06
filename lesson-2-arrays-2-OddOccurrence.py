def odd_occurrence(A):
    singleton = 0
    for element in A:
        singleton = singleton ^ element
    return singleton

print(odd_occurrence([0, 1, 2, 3]))