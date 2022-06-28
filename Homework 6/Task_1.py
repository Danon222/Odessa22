"""Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:"""

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
CC = dict(list(zip(coin, code)))
print(CC)