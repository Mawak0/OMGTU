

def Show_weigth_matrix(weigth_matrix):
    print("--------------------")
    for line in weigth_matrix:
        print(line)
    print("--------------------")

def Dijkstra(weight_matrix, start, finish):

    work_matrix = []
    for p in range(0, len(points) + 2):
        work_matrix.append([float('inf') for i in range(0, len(points) + 2)])
    work_matrix[start][len(points) + 1] = 0
    def Get_additional_weights():
        summ = 0
        for line in range(1, len(points)+1):
            if weight_matrix[line][len(points)+1] != float('inf'):
                summ += weight_matrix[line][len(points)+1]
        return summ

    def Get_current_minval_lines():
        minval_lines = []
        for line in range(1, len(points)+1):
            if work_matrix[line][len(points)] != float('inf'):
                minval_lines.append(line)
        return minval_lines
    def Process_line(line_num):
        for j in range(1, len(points)+1):
            if (j != start) and (j not in Get_current_minval_lines()):
                #print(line_num, j)
                work_matrix[line_num][j] = weight_matrix[line_num][j]+Get_additional_weights()


        minval = float('inf')
        minnext = -1
        for j in range(1, len(points) + 1):
            if weight_matrix[line_num][j] < minval:
                minval = weight_matrix[line_num][j]
                minnext = j


        work_matrix[minnext][len(points)+1] = minval
        return minnext

    minnext = Process_line(start)
    #print(minnext)
    #Show_weigth_matrix(work_matrix)
    print(Process_line(minnext))
    Show_weigth_matrix(work_matrix)
    # while minnext != finish:
    #     Process_line(minnext)
    # Show_weigth_matrix(work_matrix)







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
finish = int(input("Введите конечную точку: "))

print("Результат работы алгоритма Дейкстры: "+str(Dijkstra(weigth_matrix, start, finish)))
