# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list1 = [2, 3, 5, 9, 3]

summa = 0
for i in range(1, len(list1), 2):
        print(f"Нечётный элемент {list1[i]}") 
        summa += list1[i] 
print(f"{list1} -> Сумма элементов списка, стоящих на нечётной позиции, ответ: {summa}")