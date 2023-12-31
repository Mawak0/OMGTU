a,b,c = [int(i) for i in input().split(" ")]
s1,s2,s3 = [int(i) for i in input().split(" ")]
m1,m2,m3 = [int(i) for i in input().split(" ")]


def vektor_iz_tochek(a, b):
    vector = []
    for i in range(0, 3):
        vector.append(b[i]-a[i])
    return vector

def dlina_vectora(vector):
    dlina = 0
    for i in vector:
        dlina += i**2
    return dlina**(1/2)
#муха слева
if (m1 == 0):
    if (s1 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, m3], [s1, s2, s3]))
    if s3 == c:
        dist = dlina_vectora(vektor_iz_tochek([m2, m3, 0], [s2, c+s1, 0]))
    if s3 == 0:
        dist = dlina_vectora(vektor_iz_tochek([m2, m3, 0], [s2, -s1, 0]))
    if s2 == 0:
        dist = dlina_vectora(vektor_iz_tochek([-m2, m3, 0], [s1, s3, 0]))
    if s2 == b:
        dist = dlina_vectora(vektor_iz_tochek([m2, m3, 0], [b + s1, s3, 0]))
    if s1 == a:
        dist = min(dlina_vectora(vektor_iz_tochek([-m2, m3, 0], [a + s1, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([m2, m3, 0], [s2, c - s3 + c + a, 0])),
                   dlina_vectora(vektor_iz_tochek([m2, m3, 0], [s2, -(a + s3), 0])),
                   dlina_vectora(vektor_iz_tochek([m2, m3, 0], [b + a + b - s2, s3, 0])))
#муха вблизи
if m2 == 0:
    if (s2 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, m3], [s1, s2, s3]))
    if (s1 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m1, m3, 0], [-s2, s3, 0]))
    if (s3 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m1, m3, 0], [s1, -s2, 0]))
    if (s3 == c):
        dist = dlina_vectora(vektor_iz_tochek([m1, m3, 0], [s1, c + s2, 0]))
    if (s1 == a):
        dist = dlina_vectora(vektor_iz_tochek([m1, m3, 0], [a + s2, s3, 0]))
    if s2 == b:
        dist = min(dlina_vectora(vektor_iz_tochek([m1, m3, 0], [s1, c + b + c - s3, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, m3, 0], [a + b + a - s1, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, m3, 0], [-(b + s1), s3, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, m3, 0], [s1, -(b + s3), 0])))
#муха снизу
if m3 == 0:
    if (s3 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, m3], [s1, s2, s3]))
    if (s1 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m2, -m1, 0], [s2, s3, 0]))
    if (s2 == 0):
        dist = dlina_vectora(vektor_iz_tochek([m1, -m2, 0], [s1, s3, 0]))
    if (s1 == a):
        dist = dlina_vectora(vektor_iz_tochek([m2, m1, 0], [s2, a + s3, 0]))
    if (s2 == b):
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, 0], [s1, b + s3, 0]))
    if s3 == c:
        dist = min(dlina_vectora(vektor_iz_tochek([m1, -m2, 0], [s1, c + s2, 0])),
                   dlina_vectora(vektor_iz_tochek([m2, -m1, 0], [s2, c + s1, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, m2, 0], [s1, b + c + b - s2, 0])),
                   dlina_vectora(vektor_iz_tochek([m2, m1, 0], [s2, a + c + a - s1, 0])))
#муха сверху
if m3 == c:
    if (s3 == c): #верхняя
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, m3], [s1, s2, s3]))
    if (s1 == 0): #левая
        dist = dlina_vectora(vektor_iz_tochek([m2, c + m1, 0], [s2, s3, 0]))
    if (s2 == 0): #ближняя
        dist = dlina_vectora(vektor_iz_tochek([m1, c + m2, 0], [s1, s3, 0]))
    if (s2 == b): #дальняя
        dist = dlina_vectora(vektor_iz_tochek([m1, c + m2, 0], [s1, c + b + c - s3, 0]))
    if (s1 == a): #правая
        dist = dlina_vectora(vektor_iz_tochek([m2, c + m1, 0], [s2, c + a + c - s3, 0]))
    if (s3 == 0): #нижняя
        dist = min(dlina_vectora(vektor_iz_tochek([m2, c + m1, 0], [s2, -s1, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, c + m2, 0], [s1, -s2, 0])),
                   dlina_vectora(vektor_iz_tochek([m2, c + m1, 0], [s2, c + a + c + a - s1, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, c + m2, 0], [s1, c + b + c + b - s2, 0])))
#муха вдали
if m2 == b:
    if (s2 == b): #дальняя
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, m3], [s1, s2, s3]))
    if (s1 == 0): #левая
        dist = dlina_vectora(vektor_iz_tochek([b + m1, m3, 0], [s2, s3, 0]))
    if (s3 == 0): #нижняя
        dist = dlina_vectora(vektor_iz_tochek([b + m1, m3, 0], [s2, -s1, 0]))
    if (s3 == c): #верхняя
        dist = dlina_vectora(vektor_iz_tochek([b + m1, m3, 0], [s2, c + s1, 0]))
    if (s1 == a): #правая
        dist = dlina_vectora(vektor_iz_tochek([b + m1, m3, 0], [b + a + b - s2, s3, 0]))
    if (s2 == 0): #ближняя
        dist = min(dlina_vectora(vektor_iz_tochek([m1, c + b + c -m3, 0], [s1, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([a + b + a - m1, m3, 0], [s1, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([m1, -(b + m3), 0], [s1, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([-(b + m1), m3, 0], [s1, s3, 0])))
#муха справа
if m1 == a:
    if (s1 == a): #правая
        dist = dlina_vectora(vektor_iz_tochek([m1, m2, m3], [s1, s2, s3]))
    if (s2 == 0): #ближняя
        dist = dlina_vectora(vektor_iz_tochek([a + m2, m3, 0], [s1, s3, 0]))
        print(round(dist, 3))
        exit()
    if (s3 == 0): #нижняя
        dist = dlina_vectora(vektor_iz_tochek([m2, a + m3, 0], [s2, s1, 0]))
    if (s3 == c): #верхняя
        dist = dlina_vectora(vektor_iz_tochek([m2, c + a + c - m3, 0], [s2, c + s1, 0]))
    if (s2 == b): #дальняя
        dist = dlina_vectora(vektor_iz_tochek([b + a + b - m2, m3, 0], [b + s1, s3, 0]))
    if (s1 == 0): #левая
        dist = min(dlina_vectora(vektor_iz_tochek([m2, c + a + c - m3, 0], [s2, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([a + m2, m3, 0], [-s2, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([m2, -(a + m3), 0], [s2, s3, 0])),
                   dlina_vectora(vektor_iz_tochek([b + a + b - m2, m3, 0], [s2, s3, 0])))

out = str(round(dist, 3))
if dist == 0:
    out = "0.000"
print(out)