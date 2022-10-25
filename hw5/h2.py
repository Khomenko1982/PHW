# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Интелект
# Если второй в ответ на ход первого будет добирать до 29, то есть на 1 брать 28, на 2 брать 27 и так далее,
#  то в самом конце останется 20 конфет 
# (2021 при делении на 29 даёт в остатке 20). Начинающий проигрывает.

from random import *
import os


introduction_text = ('"Игра 2021 конфета"\n'
                'Правила игры:\n'
                'Есть всего 2021 конфет, берете их поочереди с соперником,\n'
                'За один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все оставшиеся конфеты.\n'
                )
print(introduction_text)

message = ['очередь не тормозим', 'ну же', 'по максимуму', 'оо чувствую кто то задумался',
           'быстрее уже', 'ты уснул?']

# Игра без бота

# def player_vs_player():
#     candies_total = 2021
#     max_take = 400
#     count = 0
#     player_one = input('\nВедите имя первого игрока: ')
#     player_two = input('\nВедите имя второго игрока: ')
#     print(f'\n {player_one} и  {player_two} приготовились, начинается игра!\n')
#     print('\nЖеребьевка определяет кто первый начнет игру.\n')

#     x = randint(1, 2) #Метод randint()  возвращает случайное целочисленное значение между двумя нижними и верхними пределами
#     if x == 1:
#         winner = player_one
#         loser = player_two
#     else:
#         winner = player_two
#         loser = player_one

#     print(f'Первым ходит {winner}')

    
#     while candies_total > 0:
        
#         if count % 2 == 0:
#             gamer = winner
#         else:
#             gamer = loser    
#         step = int(input(f'\n{choice(message)} {gamer} = ')) # choice()  возвращает один случайный элемент из непустой последовательности
#         if step > candies_total or step > max_take:
#                     step = int(input(
#                     f'\nВспоминаем правила, нельзя взять больше {max_take} конфет {gamer}, попробуй еще раз: '))
#         candies_total = candies_total - step
#         if candies_total > 0:
#                 print(f'\nОсталось еще {candies_total} конфет')
#                 count += 1
                
#         else:
#             print('Все  конфеты закончились')
#     print(f'Победил {gamer} !!!!')
# player_vs_player()

# игра с роботом

def player_vs_robot():
    candies_total = 2021
    max_take = 400
    player_one = input('\nВедите имя первого игрока: ')
    player_bot = 'Ботяра'
    players = [player_one, player_bot]
    print(f'\n {player_one} и  {player_bot} приготовились, начинается игра!\n')
    print('\nЖеребьевка определяет кто первый начнет игру.\n')

    winner = randint(-1, 0)

    print(f'Поздравляю {players[winner+1]} ты ходишь первым !')

    while candies_total > 0:
        winner += 1

        if players[winner % 2] == 'Ботяра':
            print(
                f'\nХодит {players[winner%2]} \nосталось {candies_total} конфет \n{choice(message)}: ')

            if candies_total < 401:
                step = candies_total
            else:
                division = candies_total//400
                step = candies_total - ((division*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 400 or step < 1:
                step = randint(1,400)
            print(step)
        else:
            step = int(input(f'\nХодит,  {players[winner%2]} \nОсталось {candies_total} конфет {choice(message)}:  '))
            while step > max_take or step > candies_total or step == 0 or step is ''   :
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'Осталось {candies_total} \nПобедил {players[winner%2]}')

player_vs_robot()


# Увеличил количество конфет за ход, а то тестировать замучаешся