
# справочник = {}

# while True:
#     print("1. Добавить контакт")
#     print("2. Найти контакт")
#     print("3. Выйти")

#     выбор = input("Введите номер действия: ")

#     if выбор == "1":
#         имя = input("Введите имя контакта: ")
#         номер = input("Введите номер контакта: ")
#         справочник[имя] = номер  
#         print("Контакт успешно добавлен!")

#     elif выбор == "2":
#         имя = input("Введите имя контакта: ")
#         if имя in справочник:
#             print("Номер контакта:", справочник[имя])
#         else:
#             print("Контакт не найден!")

#     elif выбор == "3":
#         break

#     else:
#         print("Неверный номер действия!")

# print("Справочник закрыт")



def добавить_контакт(справочник):
    имя = input("Введите имя контакта: ")
    номер = input("Введите номер контакта: ")
    справочник[имя] = номер  
    print("Контакт успешно добавлен!")

def найти_контакт(справочник):
    имя = input("Введите имя контакта: ")
    if имя in справочник:
        print("Номер контакта:", справочник[имя])
    else:
        print("Контакт не найден!")

def показать_все_контакты(справочник):
    print("Список всех контактов:")
    for имя, номер in справочник.items():
        print(имя, ":", номер)

def очистить_справочник(справочник):
    справочник.clear()
    print("Справочник успешно очищен!")

def удалить_контакт(справочник):
    имя = input("Введите имя контакта, которого хотите удалить: ")
    if имя in справочник:
        del справочник[имя]
        print("Контакт успешно удален!")
    else:
        print("Контакт не найден!")
справочник = {}

while True:
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Показать все контакты")
    print("4. Выйти")
    print("5. Удалить контакт")
    print("6. Очистить справочник")
    

    выбор = input("Введите номер действия: ")

    if выбор == "1":
        добавить_контакт(справочник)

    elif выбор == "2":
        найти_контакт(справочник)

    elif выбор == "3":
        показать_все_контакты(справочник)

    elif выбор == "4":
        break

    else:
        print("Неверный номер действия!")

print("Справочник закрыт")

