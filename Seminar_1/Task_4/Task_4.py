# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

while True:
    try:
        origami_crane = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Вы ввели НЕ число!")

print(f"Петя сделал: {origami_crane//4} журавликов, "
      f"Катя сделала: {origami_crane//2} журавликов, " 
      f"Сережа сделал {origami_crane//4} журавликов")