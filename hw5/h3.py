# Создайте программу для игры в ""Крестики-нолики"".

# Инициализация карты игрового поля
maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация выигрышных вариантов
wins = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Функция вывода на экран ячеек
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    
 
# Функция ходов
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
# Функция получения текущего результата игры
def get_result():
    win = ""
 
    for i in wins:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 
# Основная программа
game_over = False
player_one = True
 
while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 
    # 2. Куда делать ход
    if player_one == True:
        symbol = "X"
        step = int(input("Ходит Игрок1: "))
    else:
        symbol = "O"
        step = int(input("Ходит Игрок2: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определение победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player_one = not(player_one)        
 
# Игра окончена. Победитель.        
print_maps()
print("Победил", win)