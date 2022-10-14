# Реализуйте алгоритм перемешивания списка.



import random
def MixList(OriginalList):
    # Создаем копию списка
    list = OriginalList[:]
    # Цикл 
    LengthList = len(list)
    for i in range(LengthList):
        # Получаем рандомный индекс
        IndexRandom = random.randint(0, LengthList - 1)
        # Замена
        temp = list[i]
        list[i] = list[IndexRandom]
        list[IndexRandom] = temp
    # Возвращаем список
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MixedList = MixList(list)
print("Оригинальный список: ")
print(list)
print("Перемешанный список: ")
print(MixedList)

# Другой вариант, с помощью shuffle, о котором упоминали на семинаре 

import random
lst = [random.randint(0,10) for i in range(random.randint(10,20))]
print(f"Оригинальный список:\n {lst}")
random.shuffle(lst)
print(f"Перемешанный список: \n{lst}")