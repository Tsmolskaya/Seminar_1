import pandas as pa

print("\n")
file = pa.read_csv(r'Seminar_9\california_housing_train.csv')
print("---------------Выводим с 0 по 9 индексы таблицы (10 значений)-----------------\n")
print(file.head(10))

print("------------------")

# Задача 42: Узнать какая максимальная households в зоне минимального значения population

print("------------------")
print(file[file['population'] < file['population'].quantile(.25)]['households'].max())