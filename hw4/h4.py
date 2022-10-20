# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools  #  itertools.count(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step.

k = randint(2, 7)

def get_ratio(k):
    ratio = [randint(0, 10) for i in range (k + 1)]
    while ratio[0] == 0:
        ratio[0] = randint(1, 10) 
    return ratio

def get_polynom(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0] # zip_longest() модуля itertools создает итератор, который объединяет элементы из каждой итерируемой последовательности *iterables в кортежи.
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x',' x')


ratios = get_ratio(k)
polynom1 = get_polynom(k, ratios)
print(polynom1)

with open('h4.txt', 'w') as data:
    data.write(polynom1)


#  Очень сложно. Я думаю в программировании не настолько много математики что бы настолько сильно в нее углублятся)))
# Решение взято с интернета! Для себя сделал некоторые пометки на счет данной задачи, но  все расно очень трудно разобраться.