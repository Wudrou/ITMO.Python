from random import randint
import time

def name_input():
    igrok1 = input('Введите имя 1-го игрока: ')
    igrok2 = input('Введите имя 2-го игрока: ')
    return igrok1, igrok2

def game(igrok1, igrok2):
    r_count = int(input('Введите количество раундов: '))
    igrok1_Wcount = 0
    igrok2_Wcount = 0
    for i in range(r_count):
        print('Кубик бросает: ', igrok1)
        time.sleep(1)
        n1 = randint(1, 6)
        print('Выпало: ', n1)

        print('Кубик бросает: ', igrok2)
        time.sleep(1)
        n2 = randint(1, 6)
        print('Выпало: ', n2)

        if n1 > n2:
            print('Раунд выиграл ', igrok1)
            igrok1_Wcount += 1
        elif n1 < n2:
            print('Раунд выиграл ', igrok2)
            igrok2_Wcount += 1
        else:
            print('Раунд вничью')
    print(winner(igrok1, igrok2, igrok1_Wcount, igrok2_Wcount))

def winner(igrok1, igrok2, igrok1_Wcount, igrok2_Wcount):
    if igrok1_Wcount > igrok2_Wcount:
        print('Матч выиграл ', igrok1)
    elif igrok1_Wcount < igrok2_Wcount:
        print('Матч выиграл ', igrok2)
    else:
        print('Матч вичью')