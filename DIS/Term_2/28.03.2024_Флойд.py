
def Floid(weight_matrix, start, finish):
    pass


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

start = int(input("Введите начальную точку: "))
finish = int(input("Введите конечную точку: "))

print("Результат работы алгоритма Флойда:  " +str(Floid(weigth_matrix, start, finish)))
