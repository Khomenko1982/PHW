# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Задайте число: '))  

def get_fibonachi(num):
    fibo = []
    a, b = 1, 1
    for i in range(num):
        fibo.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (num+1):
        fibo.insert(0, a)  # insert (). Вставка элемента в список в заданной позиции. 
        a, b = b, a - b
    return fibo

fibo_nums = get_fibonachi(num)
print(get_fibonachi(num))
