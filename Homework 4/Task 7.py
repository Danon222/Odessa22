"""Дано два списки чисел. Надрукувати:
  - числа, що містяться одночасно як у першому списку, так і в другому
  - числа, що містяться в першому, але відсутні в другому
  - тільки унікальні для першого та другого списків"""

list_1 = (input("List 1:"))
list_2 = (input("List 2:"))
compare = list(set(list_1) & set(list_2))
dif = list(set(list_1).difference(set(list_2)))
unq = list(set(list_1 + list_2))

print(compare)
print(dif)
print(unq)
