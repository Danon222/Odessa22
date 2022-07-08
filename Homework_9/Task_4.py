"""Написати функцію яка замінить у тексті слово на інше."""


def replace_word(self: str, old: str, new: str, count: int):
    return self.replace(old, new, count)


if __name__ == '__main__':
    print(replace_word("DC makes good movies, DC makes good comics", "DC", "Marvel", 1))
    print(replace_word("DC makes good movies, DC makes good comics", "DC", "Marvel", 2))

