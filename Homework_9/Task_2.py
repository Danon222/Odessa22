"""Написати функцію яка частково приховуватиме e-mail"""


def hide_mail(email):
    name, domain = email.split('@')
    return f' Secured email: {name[:-6]}***@***{domain[3:]}'


if __name__ == '__main__':
    print(hide_mail(input("Enter your email:")))
