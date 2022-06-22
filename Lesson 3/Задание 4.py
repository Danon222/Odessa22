"""Надрукувати всі числа, які діляться на 5 без залишку, але не більше 150."""
for value in range(100,200,6):
    if value % 5 == 0 and value < 150 :
        print(value)