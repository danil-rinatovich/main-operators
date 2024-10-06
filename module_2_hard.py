import random

first_field = random.randint(3, 20)
print(first_field)
second_field = []

for i in range(1, first_field):
    for j in range(1, first_field):
        if i == j:
            continue
        elif (i + j) != 0 and first_field % (i + j) == 0:
            second_field.append([i, j])
print(second_field)
