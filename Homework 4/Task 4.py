"""По даному натуральному `n ≤ 9` виведіть драбинку з `n` сходинок, `i`-я сходинка складається з чисел від 1 до `i` без прогалин."""

n = int(input("Enter number:"))
if int(n) > 9:
    print("Wrong nubmer")
else:
  for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()




