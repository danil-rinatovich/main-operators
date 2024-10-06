import random

first_field = random.randint(3, 20)
second_field = []

for i in range(1, first_field):
    for j in range(1, i):
        if first_field % (i + j) == 0:
            second_field.append([j,i])
print(f"{first_field} - {second_field}")
