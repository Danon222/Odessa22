"""Дано рядок.
  a. Виведіть третій символ цього рядка.
  b. виведіть передостанній символ цього рядка.
  с. виведіть перші п'ять символів цього рядка.
  d. виведіть весь рядок, крім двох останніх символів.
  e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи
  з першого).
  f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
  g. виведіть усі символи у зворотному порядку.
  h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
  i. виведіть довжину цього рядка."""

print("Enter something:")
a = input()
print("3й символ рядка:", a[2])
print("Первые 5 символов:", a[0:5])
print("Кроме 2х последних символов:", a[:-2])
print("Парные индексы:", a[::2])
print("Не парные индексы:", a[1::2])
print("В обратном порядке:", a[::-1])
print("Через 1 в обратном порядке:", a[-1::-2] )
print("Длина рядка :", len(a), "символов")
