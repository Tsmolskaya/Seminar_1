# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Введите длинну шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("На сколько долек будем делить: "))


def ChocolateSeparate(n, m, k):
    if k < m*n and (k % m == 0 or k % n == 0):
        print("Шоколадка разделена, все довольны!")
    else:
        print("Так как шоколадка не делится, то никто её не получит!")


ChocolateSeparate(n, m, k)