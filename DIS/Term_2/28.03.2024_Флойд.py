
def Show_weigth_matrix(weigth_matrix):
    print("--------------------")
    for line in weigth_matrix:
        print(line)
    print("--------------------")

def get_point_inputs(weigth_matrix, point):
    point_inputs = []
    for p in range(0, len(points)+1):
        if weigth_matrix[p][point] != float("inf"):
            point_inputs.append(p)
    return point_inputs

def Floid(weight_matrix, start, finish):
    for e in full_edges:
        next[e[0]][e[1]] = e[1]
    for p in points:
        next[p][p] = p
    matrix = []
    matrix.append(weight_matrix[:])
    for prom in range(1, len(points)+1):
        matrix.append(empty_matrix[:])
        for a in range(1, len(points)+1):
            for b in range(1, len(points)+1):
                #Show_weigth_matrix(matrix[prom])
                if matrix[prom-1][a][prom]+matrix[prom-1][prom][b] < matrix[prom-1][a][b]:
                    next[a][b] = next[a][prom]
                matrix[prom][a][b] = min([matrix[prom-1][a][b], matrix[prom-1][a][prom]+matrix[prom-1][prom][b]])
    Show_weigth_matrix(matrix[-1])
    print("Путь между вершинами "+str(start)+" и "+str(finish)+" = "+str(matrix[-1][start][finish]))
    path = []
    if next[start][finish] != float("inf"):
        path.append(start)
        u = start
        v = finish
        while u != v:
            u = next[u][v]
            path.append(u)
    print(path)


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
empty_matrix = []
next = []

for p in range(0, len(points ) +1):
    weigth_matrix.append([float('inf') for i in range(0, len(points ) +1)])
    empty_matrix.append([float('inf') for i in range(0, len(points ) +1)])
    next.append([float('inf') for i in range(0, len(points ) +1)])

full_edges = []
for e in edges:
    weigth_matrix[e[0]][e[1]] = e[2]
    weigth_matrix[e[1]][e[0]] = e[2]
    full_edges.append(e)
    full_edges.append([e[1], e[0], e[2]])


start = int(input("Введите начальную точку: "))
finish = int(input("Введите конечную точку: "))

Floid(weigth_matrix, start, finish)
