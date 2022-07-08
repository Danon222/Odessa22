"""Написати функцію, яка рахуватиме кількість очок футбольної команди.

Перемога дає 3 очки, нічия 1 очко, поразка -1 очко.
Функція приймає три аргументи – win, draw, loss."""


def counter(win: int, draw: int, loss: int):
    return win * 3 + draw - loss


if __name__ == '__main__':
    print("Total points:", counter(5, 6, 2))