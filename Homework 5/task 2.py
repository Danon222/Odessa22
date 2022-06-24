"""2. Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів.
"""

text1 = input("Enter some text:")
text2 = text1.split()
l = len(text2)
print("Amount of words in text :", l)
print("Amount of symbols in Text:", len([i for i in text1 if i.isalpha() + i.isdigit()]))
