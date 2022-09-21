# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random as rand
import re
import mylib

mylib.init()

# Инициализация магических чисел
min_candies      = 30
min_step_candies = 2
max_step_candies = 28
#---------------------------


def GetSetting():
    '''Получение первоначальных настроек'''
    print(f"Ведите общее число конфет не мене {min_candies-1} штук")
    numbers_of_candies = mylib.GetIntWithLowLimit(min_candies)
    print(f"Ведите число конфет заход, но не менее {min_step_candies} и не более {max_step_candies} штук")
    step_candies = mylib.GetIntWithLowAndHightLimit(min_step_candies, max_step_candies)
    return step_candies, numbers_of_candies

def GetWhoisfirst(namePlayer1, namePlayer2):
    '''Кидаем жребий кто ходит первый'''
    player = rand.choice([True, False])
    return namePlayer1 if player else namePlayer2

def player_vs_player(numbers_of_candies, step_candies):
    '''Режим игрока против игрока'''
    player = GetWhoisfirst("Первый", "Второй") # Кидаем монетку 
    while numbers_of_candies > 1:
        print(f'Сейчас, в банке {numbers_of_candies}')
        print(f"Ходит {player} игрок!" + '\n' + f"Сколько конфет Вы забирает? Но не более {step_candies}")
        if player == "Первый":
            x1 = mylib.GetIntWithLowAndHightLimit(1, step_candies)
            numbers_of_candies -= x1
            if numbers_of_candies == 1:
                return f'Победа {player}'
            player = "Второй"
        else:
            x2 = mylib.GetIntWithLowAndHightLimit(1, step_candies)
            numbers_of_candies -= x2
            if numbers_of_candies == 1:
                return f'Победа {player}'
            player = "Первый"
    return f'Победил {player} игрок'

def player_vs_skynet(numbers_of_candies, step_candies):
    '''Режим игрока против скайнета'''
    player = GetWhoisfirst("Человека", "Скайнета") # Кидаем монетку 
    while numbers_of_candies > 1:
        print()
        print(f'Сейчас, в банке {numbers_of_candies}')
        print(f"Ход {player}!" + '\n' + f"Сколько конфет Вы забирает? Но не более {step_candies}")
        if player == "Человека":
            x1 = mylib.GetIntWithLowAndHightLimit(1, step_candies)
            numbers_of_candies -= x1
            if numbers_of_candies == 1:
                return f'Победа {player}'
            player = "Скайнета"
        else:
            x2 = rand.randint(1, step_candies+1)
            print(f'Скайнет решил забрать {x2} конфет')
            numbers_of_candies -= x2
            if numbers_of_candies == 1:
                return f'Победа {player}'
            player = "Человека"
    return f'Победа {player}'

def player_vs_bot(numbers_of_candies, step_candies):
    '''Режим игрока против скайнета'''
    player = GetWhoisfirst("Человека", "Скайнета") # Кидаем монетку 
    while numbers_of_candies > 1:
        print()
        print(f'Сейчас, в банке {numbers_of_candies}')
        print(f"Ход {player}!" + '\n' + f"Сколько конфет Вы забирает? Но не более {step_candies}")
        if player == "Человека":
            x1 = mylib.GetIntWithLowAndHightLimit(1, step_candies)
            numbers_of_candies -= x1
            if numbers_of_candies == 1:
                return f'Победа {player}'
            player = "Скайнета"
        else:
            if numbers_of_candies > step_candies:
                for i in range(1,step_candies,1):
                    if  i % 3 == 0 :
                        x2 = i
                        break
            else:
                x2 = numbers_of_candies - 1
            print(f'Скайнет решил забрать {x2} конфет')
            numbers_of_candies -= x2
            if numbers_of_candies == 1:
                return f'Победа {player}'
            player = "Человека"
    return f'Победа {player}'

def mainCycle():
    print("Битва умов.")
    print()
    print("Выберете себе противника: \n \
    1 - Игрок против игрока          \n \
    2 - Игрок против простого бота   \n \
    3 - Игрок против 'умного' бога   \n \
    4 - Выход ")
    print()
    againstWho = mylib.GetIntWithLowAndHightLimit(1, 4)
    if againstWho == 4:
        print("Прощайте")
        return
    step_candies, numbers_of_candies = GetSetting()
    if againstWho == 1:
        winner = player_vs_player(numbers_of_candies, step_candies)
    elif againstWho == 2:
        winner = player_vs_skynet(numbers_of_candies, step_candies)
    elif againstWho == 3:
        winner = player_vs_bot(numbers_of_candies, step_candies)  
    print(winner)


mainCycle()


