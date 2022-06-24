"""Написати функцію яка прибере з dict елементи із значеннями None:"""

dict_1 = {'first_color': 'Red', 'second_color': None, 'third_color': 'Green', 'Fourth_color': None}
print(dict_1)
dict_1 = {key: val for key, val in dict_1.items() if val != None}
print(dict_1)




