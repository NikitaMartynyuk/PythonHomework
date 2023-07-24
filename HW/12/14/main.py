# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
# нужно перевернуть




# def minCoinsToFlip(coins):
#     heads = 0
#     tails = 0
    
#     for coin in coins:
#         if coin == "H":
#             heads += 1
#         elif coin == "T":
#             tails += 1
    
#     return min(heads, tails)

# coins = ["H", "T", "H", "T", "H"]
# print(minCoinsToFlip(coins))  




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.




# S = int(input("Введите сумму чисел: "))
# P = int(input("Введите произведение чисел: "))

# found_solution = False

# for x in range(1, 1001):
#     for y in range(1, 1001):
#         if x + y == S and x * y == P:
#             print("Задуманные числа: ", x, "и", y)
#             found_solution = True
#             break
#     if found_solution:
#         break

# if not found_solution:
#     print("Не угадал.")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

def print_powers_of_two(N):
    power = 0
    result = 1
    
    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

N = int(input("Введите число N: "))

print("Целые степени двойки, не превосходящие", N, ":")
print_powers_of_two(N)