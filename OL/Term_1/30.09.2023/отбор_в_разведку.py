def find_a_b(c):
    a = 1
    while a < c:
        a *= 2
    b = a
    a = a // 2
    return a, b

x = int(input())
a, b = find_a_b(x)
max_pos = a + (b-a)/2
if x > max_pos:
    rez = b - x
elif x < max_pos:
    rez = x - a
else:
    rez = (b-a)/2
print(rez)



