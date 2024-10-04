first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))

if first == second and first == third and second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
else:
    print(2)
