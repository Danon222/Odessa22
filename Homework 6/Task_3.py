"""Дано перелік значень. Повернути словник, де кожен ключ - це індекс листа,
  а значення листа – це значення ключа:"""

list_1 = ['a', 'b', 'c', 'd', 'e']
dict_1 = {index: value for index, value in enumerate(list_1)}
print(dict_1)