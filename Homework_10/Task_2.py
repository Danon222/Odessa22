"""Написати функцію, яка визначить, чи є введений текст паліндромом (той який читається однаково з будь-якого боку),
приклад:
Шалаш, зараз, Дід, Піп, 13231
Паліндром — і ні морд, ні лап"""

from string import punctuation


def delete_punctuation(text):
    new_text = text.translate(str.maketrans("", "", punctuation))
    return new_text.replace(" ", "").lower()


def palindrome(text):
    return delete_punctuation(text) == delete_punctuation(text[::-1])


def main():
    print(palindrome((input("Enter text:"))))


if __name__ == '__main__':
    main()


