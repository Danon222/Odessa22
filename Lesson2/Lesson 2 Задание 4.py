
a = int(input('введите год:'))
if a % 4 == 0 and a % 100 != 0 and a % 400 != 0:
    print("YES")
else:
    print("NO")
