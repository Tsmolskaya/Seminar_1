import pandas as pa

print("\n")
file = pa.read_csv(r'Seminar_9\california_housing_train.csv')

print("---------------Выводим с 0 по 9 индексы таблицы (10 значений)-----------------\n")
print(file.head(10))

print("------------------")

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

print(file[file["population"] <= 500].median())
print("\n")
print("---------------Средняя стоиомсть дома с населением до 500------------------\n")
middle_price = file[file["population"] <= 500].median()
print(middle_price.median_house_value)