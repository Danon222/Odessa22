""" Користувач вводить число від 1 до 10, програма генерує рандомне число від 1 до 10, якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'. Дати користувачеві три спроби;)"""


import random
count = 0
number = random.randint(1, 10)
while count < 3:
    guess = int(input('Enter nubmer: '))
    count += 1

    if guess < number:
        print('You lose')

    if guess > number:
        print('You lose')

    if guess == number:
        break


if guess == number:
    print('You WON')

