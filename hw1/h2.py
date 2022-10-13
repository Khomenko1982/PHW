# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


a = int(input('Введите число a '))
b = int(input('Введите число b '))
c = int(input('Введите число c '))

first = a * b * c
two = a + b + c

if first > 0:
    first = 0
elif first < 1:
    first = 1
if b > 0:
    b = 1
elif b < 1:
    b = 1

if first == two:
    print('Утверждение истинно')
elif first != two:
    print('Утверждение ложно')

firstSide = not (a or b or c)
twoSide = not a and not b and not c
res = firstSide == twoSide

if res == True:
    print('Истина')
else:
    print('Ложь')