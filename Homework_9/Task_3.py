"""Написати функцію яка поверне найдовше слово у рядку:"""


def longest_word(text):
    word = max(text.split(), key=len)
    return word


def text():
    sentence = input("Enter text:")
    print("The longest word in text is :", longest_word(sentence))


if __name__ == '__main__':
    text()
