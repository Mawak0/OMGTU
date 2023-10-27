
n = int(input())
details_raw = []
for i in range(0, n):
    details_raw.append([int(q) for q in input().split()])

details = []
for i in range(0, n):
    a = details_raw[i]
    details.append([a[0:5] , a[5:10], a[10:15], a[15:20]])

forms_raw = []
for i in range(0, n*2):
    forms_raw.append([int(q) for q in input().split()])

forms = []
for i in range(0, n*2):
    a = forms_raw[i]
    forms.append([a[0:5] , a[5:10], a[10:15]])

print(details)
print(forms)

def match(form1, form2, detail):
    #проверяет, подходит ли формы для детали, переворачивая вторую форму перед первой
    #выступы детали - верхняя, ближняя, нижняя, дальняя
    #выемки форм - верхняя, вдавленная, нижняя
    for i in range(0, len(form2)):
        form2[i].reverse()
    print("----------------------------------------")
    print(form1)
    print(form2)
    print(detail)
    if (detail[0] == form1[0] == form2[0]):
        if (detail[1] == form2[1]):
            if (detail[2] == form2[2] == form1[2]):
                if (detail[3] == form1[1]):
                    return True
    return False

def rotate_detail(detail):
    return [detail[3], detail[0], detail[1], detail[2]]

def turn_over_detail(detail):
    return [reversed(detail[0]), reversed(detail[3]), reversed(detail[2]), reversed(detail[1])]

print(match(forms[1], forms[2], details[1]))
pairs = []




# деталь имеет 8 позиций (4 по кругу,  + переворачиваем(отзеркаливаем) - это создаст еще 4 по кругу)
# одну форму переворачиваем(отзеркаливаем) и вращаем два раза + под ней форму вращаем один раз
