# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('h5_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('h5_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('h5_1.txt','r') as file:
    polynom_1 = file.readline()
    list_polynom_1 = polynom_1.split()


with open('h5_2.txt','r') as file:
    polynom_2 = file.readline()
    list_polynom_2 = polynom_2.split()

print(f'Сумма многочленов: {list_polynom_1} + {list_polynom_2}')
sum_poly = list_polynom_1 + list_polynom_2

with open('h5_summ.txt', 'w', encoding='utf-8') as file:
    file.write(f' {list_polynom_1} + {list_polynom_2}')


# Если я правильно понял, для реального сложения двух многочленов, а не текстовой строки, необходимо в уравнении
#  оставить только числа в виде строки и затем последовательно складывать получившиеся элементы двух списков,
#   первый элемент списка 1 с первым элементом списка 2.  Для меня это пока слишком сложно.
