import math
import statistics

#print(help(math))
#print(help(statistics))

list = [14, 43, 27, 1, -9, 56, 90, 11, 9, 176]
print(list)
print("Сумма чисел: ", math.fsum(list))
print("Среднее значение: ", statistics.mean(list))
print("Медиана: ", statistics.median(list))
print("Стандартное отклонение: ", statistics.stdev(list))

import random

print("Случайное число от 1 до 100: ", random.randint(1, 100))
