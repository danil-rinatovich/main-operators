import random

first_field = 20#random.randint(3, 20)
second_field = []

for i in range(1, first_field):
    for j in range(i + 1, first_field):
        if first_field % (i + j) == 0:
            second_field.append([i, j])
print(f"{first_field} - {second_field}")
