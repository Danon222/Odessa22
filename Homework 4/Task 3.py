"""Дано два цілих числа 'A' і 'В'. Виведіть усі числа від `A` до `B` включно, в порядку зростання, якщо `A < B`, або в порядку зменшення в іншому випадку."""

a = int(input("A:"))
b = int(input("B:"))
if (a < b):
 for i in range(a, b + 1, 1):
   print(i, end=",")
else:
 for i in range(a, b - 1, -1):
   print(i, end=",")




