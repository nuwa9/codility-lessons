def missing_element(A):
    return int((len(A) * len(A) + 3 * len(A))/2 + 1 - sum(A))

print(missing_element([2, 3, 1, 4, 5, 6, 7, 9]))