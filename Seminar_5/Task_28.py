# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))


def sum(a, b):
    return a if b == 0 else sum(a+1, b-1) if b > 0 else sum(a-1, b+1)

print(sum(a, b))