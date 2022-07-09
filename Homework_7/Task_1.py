"""1. Дано два списки чисел. Порахуйте, скільки чисел міститься як у першому списку, і у другому. (set)
"""

list_1 = {1, 3, 5, 7, 8, 6, 1, 1, 1, 1, 106, 54, 2}
list_2 = {2, 1, 99, 55, 3, 8, 33, 22}
list_3 = list(list_1.intersection(list_2))
print("Same numbers in both lists:", list_3)
print("Amount of same numbers:", len(list_3))

