# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform  # uniform () возвращает случайное число с плавающей запятой в заданном интервале.


elem = int(input('Введите количество элементов списка: '))
list1 = []
for i in range(elem):
    rndm = uniform(0, 9)
    list1.append(round(rndm, 2)) #append  добавляет элемент в конец списка.

min = list1[0]%1
max = 0
for i in range(len(list1)):
    
    if max < list1[i]%1:
        max = list1[i]%1
    if min > list1[i]%1:
        min = list1[i]%1
difference = (max - int(max)) - (min - int(min))

print(list1)
print(round(max,2),round(min,2))
print(round(difference,2)) # Round  округляет число с плавающей точкой до той цифры, которую задает пользователь. 

