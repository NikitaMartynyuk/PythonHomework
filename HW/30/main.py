# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# n = int(input("Введите количество элементов: "))
# a1 = int(input("Введите первый элемент: "))
# d = int(input("Введите разность: "))

# progression = []

# for i in range(n):
#     progression.append(a1 + i * d)

# print(progression)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)



def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

my_list = [1, 5, 2, 7, 4, 8, 3, 6, 9]
min_value = 3
max_value = 7

result = find_indexes(my_list, min_value, max_value)
print(result)

