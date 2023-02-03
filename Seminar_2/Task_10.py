# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:

# 5 -> 1 0 1 1 0
# 2

from random import randint

n = int(input("Введите количество монеток: "))
list = []
orel = 0
reshka = 0

# Генерируем список, в котором 0 = решка, 1 орел
def list_generate(n):
    for i in range(n):
        if i < n:
            list.append(randint(0, 1))
    return list

# Определяем количество переворачиваний и выводим результат
def change_position_monedas(list, orel, reshka):
    for i in range(len(list)):
        if list[i] == 1:
            orel += 1
    print("Количество перекладываний для решки:", orel,
          "Количество перекладываний для орла:", (len(list)) - orel)
    print("Минимальное количество перекладываний:"
          , orel if orel < len(list) - orel else (len(list)) - orel)


print("Список перевернутых и неперевернутых монеток:", list_generate(n))
change_position_monedas(list, orel, reshka)