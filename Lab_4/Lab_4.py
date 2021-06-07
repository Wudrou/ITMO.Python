from random import randint
import time

#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего: ')
igrok2 = input('Введите имя 2-го играющего: ')

r_count = int(input('Установи количество раундов: '))

igrok1_Wcount = 0
igrok2_Wcount = 0

for i in range(r_count):
    #Моделирование бросания кубика первым играющим
    print('Кубик бросает: ', igrok1)
    time.sleep(1)
    n1 = randint(1, 6)
    print('Выпало: ', n1)

    #Моделирование бросания кубика вторым играющим
    print('Кубик бросает: ', igrok2)
    time.sleep(1)
    n2 = randint(1, 6)
    print('Выпало: ', n2)

    #Определение результата (3 возможных варианта)
    if n1 > n2:
        print('Раунд выиграл ', igrok1)
        igrok1_Wcount += 1
    elif n1 < n2:
        print('Раунд выиграл ', igrok2)
        igrok2_Wcount += 1
    else:
        print('Раунд вничью')

if igrok1_Wcount > igrok2_Wcount:
    print('Матч выиграл ', igrok1)
elif igrok1_Wcount < igrok2_Wcount:
    print('Матч выиграл ', igrok2)
else:
    print('Матч вичью')
