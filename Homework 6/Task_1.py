"""Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:"""


def key_value(key: tuple, value: tuple) -> dict:
    dict_1 = {k: item for k, item in zip(key, value)}
    return dict_1


def main():
    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')
    print(key_value(coin, code))


if __name__ == "__main__":
    main()