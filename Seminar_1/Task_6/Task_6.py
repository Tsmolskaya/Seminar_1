# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

while True:
    try:
        number = int(input("Введите шестизначное число: "))
        break
    except ValueError:
        number = print("Введенные символы не являются числом: ")
        
def Integer(number):
    while len(str(number)) != 6:
        number = int(input("Повнимательнее, посчитайте количество введенных символов: "))
    else:
        return number

def CreateList(number):
    number_str = str(number)
    list = []
    for i in number_str:
        list.append(int(i))
    if list[0] + list[1] + list[2] == list[3] + list[4] + list[5]:
        print("У Вас счастливый билет, скорее скушайте его!")
    else:
        print("Ваш билет не счастливый, не вздумайте его съесть!")

         
Integer(number)


CreateList(number)
