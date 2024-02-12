

def prima(edges):
    cost = 0
    points = set()
    def s(i):
        return i[2]

    edges.sort(key=s)
    for e in edges:
        points.add(e[0])
        points.add(e[1])
    points = list(points)
    def done(points, a_points):
        flag = True
        for p in points:
            if p not in a_points:
                flag = False
        return flag
    a_points = [points[0]]
    while not done(points, a_points):
        for e in edges:
            if ((e[0] in a_points) and (e[1] not in a_points)):
                a_points.append(e[1])
                cost += e[2]
                break
            elif ((e[1] in a_points) and (e[0] not in a_points)):
                a_points.append(e[0])
                cost += e[2]
                break
    return(cost)





edges = []
edges_count = int(input("Введите кол-во ребер графа: "))
print("Вводите информацию о ребрах в следующем виде: ")
print("1 2 3")
print("где 1 и 2 - вершины, соединяемые ребром")
print("3 - вес ребра")
print("после каждой такой записи нажимайте enter")
for i in range(0, edges_count):
    edges.append([int(q) for q in input().split(" ")])
print("Результат работы алгоритма Прима: "+str(prima(edges)))

