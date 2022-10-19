# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint  # randint(): возвращает случайное число из определенного диапазона


number = int(input('Введите количество элементов списка: '))
list1 = []
list2 = []

for i in range(number):  # Range() является универсальной функцией питона для создания списков (list) содержащих арифметическую прогрессию. Чаще всего она используется в циклах for.
    list1.append(randint(0, 9))  # Метод append () в Python добавляет элемент в конец списка.

for i in range(len(list1)):
    while i < len(list1)/2 and number > len(list1)/2:
        number = number - 1
        a = list1[i] * list1[number]
        list2.append(a)
        i += 1

print(list1)
print(list2)