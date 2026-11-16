import random

def passing_cars(A):
    pairs = 0
    west_cars = 0
    for value in A:
        if value == 0:
            west_cars += 1
        elif pairs < 1000000000:
            pairs += west_cars
        else:
            return -1
    return pairs

print(passing_cars(random.choices([0, 1], k=10000)))

print(passing_cars([0, 1, 0, 1, 1]))