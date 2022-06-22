# First point
a = int(input("a"))
b = int(input("b"))

# Second point
aa = int(input("aa"))
bb = int(input("bb"))

# subtraction
sub_a = a - aa
sub_b = b - bb

if sub_a < 0:
    sub_a = -sub_a
if sub_b < 0:
    sub_b = -sub_b

if a == b == aa == bb:
    print('The same point')
elif a <= 0 or b <= 0 or aa <= 0 or bb <= 0 or a > 8 or aa > 8 or b > 8 or bb > 8:
    print('Error, wrong point')

if sub_a == 1 and sub_b == 2 or sub_a == 2 and sub_b == 1:
    print('Yes')
else:
    print('No')