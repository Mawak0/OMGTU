
def Show_weigth_matrix(weigth_matrix):
    print("--------------------")
    for line in weigth_matrix:
        print(line)
    print("--------------------")

def get_min_mark_point(marks, checked_points):
    min_val = float("inf")
    key = ""
    for e in marks.items():
        if e[0] not in checked_points:
            if e[1] < min_val:
                min_val = e[1]
                key = int(e[0])
    return [key, min_val]

def get_neighbours(points, weight_matrix, point):
    neighbours = []
    for j in range(1, len(points) +1):
        if weight_matrix[int(point)][j] != float('inf'):
            neighbours.append(j)
    return neighbours

def Dijkstra(points, weight_matrix, start, finish):
    checked_points = []
    marks = dict()
    for p in points:
        if p == start:
            marks[p] = 0
        else:
            marks[p] = float("inf")
    while (len(points) != len(checked_points)) and (finish not in checked_points):
        min_mark_point, min_mark = get_min_mark_point(marks, checked_points)
        if min_mark_point == "":
            print("Добраться невозможно")
            return -1
        neighbours = get_neighbours(points, weight_matrix, min_mark_point)
        for nei in neighbours:
            if nei not in checked_points:
                if marks[nei] > min_mark +weight_matrix[min_mark_point][nei]:
                    marks[nei] = min_mark +weight_matrix[min_mark_point][nei]
        checked_points.append(min_mark_point)
    return marks[finish]


def work():
    edges = []
    print("Введите информацию о аэропортах в виде графа")
    edges_count = int(input("Введите кол-во ребер графа: "))
    print("Вводите информацию о ребрах в следующем виде: ")
    print("1 2 3")
    print("где 1 и 2 - вершины (аэропорты), соединяемые ребром (возможностью перелета)")
    print("3 - вес ребра (длительность перелета)")
    print("после каждой такой записи нажимайте enter")

    try:
        for i in range(0, edges_count):
            edges.append([int(q) for q in input().split(" ")])
            edges[-1][2] = edges[-1][2] + 1  # учитываем время пересадки
    except:
        print("Данные введены в неверном формате")
        return

    points = set()
    for e in edges:
        points.add(e[0])
        points.add(e[1])

    weigth_matrix = []
    for p in range(0, len(points ) +1):
        weigth_matrix.append([float('inf') for i in range(0, len(points ) +1)])

    for e in edges:
        weigth_matrix[e[0]][e[1]] = e[2]

    start = int(input("Введите начальную точку (аэропорт отправления): "))
    finish = int(input("Введите конечную точку (аэропорт назначения): "))
    if start not in points:
        print("Аэропорт отправления отсутствует в введенном графе")
        return
    if finish not in points:
        print("Аэропорт назначения отсутствует в введенном графе")
        return
    time = Dijkstra(points, weigth_matrix, start, finish)
    if time != -1:
        time -= 1 # учитываем, что начало маршрута не считается пересадкой
    print("Суммарное время маршрута:  " +str(time))

def menu():
    while True:
        c = int(input("1) Вычисление\n2) Описание задачи\n3) Данные об авторе\n4) Выход\n>"))
        if c == 1:
            work()
            input("Нажмите любую кнопку для выхода в главное меню")
        elif c == 2:
            print("Программа вычисляет кратчайший по времени перелета маршрут из одного аэропорта в другой, используя алгоритм Дейкстры.\nАэропорты и возможности перелетов задаются в виде матрицы.")
            input("Нажмите любую кнопку для выхода в главное меню")
        elif c == 3:
            print("Автор программы: Дрожжачих А.Д. ФИТ-231")
            input("Нажмите любую кнопку для выхода в главное меню")
        elif c == 4:
            return
        else:
            print("Выбрана неверная опция")

menu()