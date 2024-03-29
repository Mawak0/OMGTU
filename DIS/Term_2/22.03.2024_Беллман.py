def Show_weigth_matrix(weigth_matrix):
    print("--------------------")
    for line in weigth_matrix:
        print(line)
    print("--------------------")

def Show_work_matrix(work_matrix):
    for line in range(1, len(work_matrix)):
        print(work_matrix[line])

def get_point_inputs(weigth_matrix, point):
    point_inputs = []
    for p in range(0, len(points)+1):
        if weigth_matrix[p][point] != float("inf"):
            point_inputs.append(p)
    return point_inputs


def Bellman(weight_matrix, start):

    work_matrix = []
    for p in range(0, len(points) + 1):
        if p != start:
            work_matrix.append([float("inf")])
        else:
            work_matrix.append([0])

    stop = False
    k = 0


    while not stop:
        k += 1
        for la in range(1, len(points)+1):
            if la != start:
                min_lambda = float("inf")
                for j in range(1, len(points)+1): # get min lambda
                    if (min_lambda > work_matrix[j][k-1]+weight_matrix[j][la]):
                        min_lambda = work_matrix[j][k-1]+weight_matrix[j][la]
            else:
                min_lambda = 0
            work_matrix[la].append(min_lambda)
        if k == len(points)+1:
            stop = True
    not_ident = False
    for i in range(1, len(points)):
        if work_matrix[i][k] != work_matrix[i][k-1]:
            not_ident = True
    if not_ident:
        print("В графе содержится контур отрицательного веса")
    else:
        print("Минимальные расстояния от вершины "+str(start)+" до остальных вершин")
        for i in range(1, len(points)+1):
            print("до "+str(i)+" вершины : "+str(work_matrix[i][-1]))
        back_ways = []
        for i in range(0, len(points)):
            back_ways.append([list(points)[i]])

        for s in range(1, len(points) + 1):
            search_depth = 0
            while (back_ways[s - 1][-1] != start) and (len(points) - 2 - search_depth != -1):
                ss = back_ways[s - 1][-1]
                inputs = get_point_inputs(weigth_matrix, ss)
                for r in inputs:
                    if (work_matrix[r][len(points) - 2 - search_depth] + weight_matrix[r][ss] == work_matrix[ss][
                        len(points) - 1 - search_depth]):
                        back_ways[s - 1].append(r)
                        break
                search_depth += 1
        print("Пути от вершины " + str(start) + " до остальных вершин:")
        for way in back_ways:
            path = ""
            for w in way[::-1]:
                path = path + " 🢡 " + str(w)
            print("до вершины " + str(way[0]) + " : " + path)


















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


for p in range(0, len(points)+2):
    weigth_matrix.append([float('inf') for i in range(0, len(points)+2)])


for e in edges:
    weigth_matrix[e[0]][e[1]] = e[2]

start = int(input("Введите начальную точку: "))

Bellman(weigth_matrix, start)
