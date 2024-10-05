import random

random_number = random.randint(3, 20)
print(random_number)
list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
password = []
for i in range(0, len(list_) + 1):
    for j in range(0, i):
        if i + j == random_number and i + j % random_number:
            password.append((i, j))
            break
print(password)

