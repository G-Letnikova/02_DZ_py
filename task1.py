# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("введите число монеток: "))
orel = 0
reshka = 0
for i in range(n):
    monet = random.randint(0, 1)
    print(monet, end=", ")
    if monet == 0:
        orel += 1
    else:
        reshka += 1
print()
print(orel if orel > reshka else reshka)