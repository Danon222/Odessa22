"""Даний перелік випадкових цілих чисел. Замініть усі непарні числа списку нулями. І виведете їхню кількість.
"""

some_range = list(range(1, 50, 1))
print("Original list:", some_range)
for n, i in enumerate(some_range):
    if i % 2 != 0:
        some_range[n] = 0
print("All odds numbers changed to 0 :", some_range)
count = some_range.count(0)
print("Amount of 0 in list = ", count)




