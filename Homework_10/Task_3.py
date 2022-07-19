"""Написати функцію яка зрушить отриманий список на N елементів вправо або вліво, аргументи,
   що приймаються - список і натуральне число(якщо негативне зрушуємо вліво, позитивне - вправо)."""


def shift(lst, steps):
    if steps < 0:
        for i in range(abs(steps)):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


list_1 = [3, 4, 5, 6, 7, 8, 9, 10]
print(list_1)

shift(list_1, 2)
print(list_1)

list_2 = [3, 4, 5, 6, 7, 8, 9, 10]
shift(list_2, -3)
print(list_2)

