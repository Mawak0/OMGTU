
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

def get_neighbours(weight_matrix, point):
    neighbours = []
    for j in range(1, len(points) +1):
        if weight_matrix[int(point)][j] != float('inf'):
            neighbours.append(j)
    return neighbours

def Dijkstra(weight_matrix, start, finish):
    # Show_weigth_matrix(weight_matrix)
    checked_points = []
    marks = dict()
    back_way = dict()
    for p in points:
        if p == start:
            marks[p] = 0
            back_way[p] = p
        else:
            marks[p] = float("inf")
    while (len(points) != len(checked_points)) and (finish not in checked_points):
        # while (len(points) != len(checked_points)):
        min_mark_point, min_mark = get_min_mark_point(marks, checked_points)
        neighbours = get_neighbours(weight_matrix, min_mark_point)
        for nei in neighbours:
            if nei not in checked_points:
                if marks[nei] > min_mark +weight_matrix[min_mark_point][nei]:
                    marks[nei] = min_mark +weight_matrix[min_mark_point][nei]
                    back_way[nei] = min_mark_point
                #marks[nei] = min([marks[nei], min_mark +weight_matrix[min_mark_point][nei]])
        checked_points.append(min_mark_point)
    print("Ребра, входящие в минимальное остовное дерево: "+str(back_way))
    return marks[finish]

edges = []
edges_count = int(input("Введите кол-во ребер графа: "))
print("Вводите информацию о ребрах в следующем виде: ")
print("1 2 3")
print("где 1 и 2 - вершины, соединяемые ребром")
print("3 - вес ребра")
print("после каждой такой записи нажимайте enter")

for i in range(0, edges_count):
    edges.append([int(q) for q in input().split(" ")])

points = set()
for e in edges:
    points.add(e[0])
    points.add(e[1])

weigth_matrix = []


for p in range(0, len(points ) +1):
    weigth_matrix.append([float('inf') for i in range(0, len(points ) +1)])


for e in edges:
    weigth_matrix[e[0]][e[1]] = e[2]
    weigth_matrix[e[1]][e[0]] = e[2]
Show_weigth_matrix(weigth_matrix)
start = int(input("Введите начальную точку: "))
finish = int(input("Введите конечную точку: "))

print("Результат работы алгоритма Дейкстры:  " +str(Dijkstra(weigth_matrix, start, finish)))
