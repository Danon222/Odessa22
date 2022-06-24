"""Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000, і повертає `True`, якщо воно просте, і `False` - інакше.
(Прості числа - ті які діляться без залишку тільки на себе або 1, наприклад 2, 3, 5, 7, 11 ...)"""


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = n ** (1 / 2)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


print(is_prime(int(input("Enter number: "))))