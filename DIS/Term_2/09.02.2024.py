def kruskal(edges):

    cost = 0
    def s(i):
        return i[2]
    edges.sort(key=s)
    classes =[]

    def cross(a,b):
        for i in range(0, len(a)):
            if a[i] in b:
                return True
        return False

    def merge(a,b):
        a = list(set(a+b))
        return a

    points = set()
    for e in edges:
        points.add(e[0])
        points.add(e[1])
    for e in edges:
        find = 0
        for c in range(0, len(classes)):
            if (e[0] in classes[c]) and (e[1] not in classes[c]):
                classes[c].append(e[1])
                cost += e[2]
                find = 1
                break
            elif (e[1] in classes[c]) and (e[0] not in classes[c]):
                classes[c].append(e[0])
                cost += e[2]
                find = 1
                break
            elif ((e[1] in classes[c]) and (e[0] in classes[c])):
                find = 1
                break
        if find == 0:
            classes.append([e[0],e[1]])
            cost += e[2]

        try:
            for c1 in range(0, len(classes)):
                for c2 in range(0, len(classes)):
                    if (c1 != c2) and (c1 > c2):
                        if cross(classes[c1], classes[c2]):
                            classes[c1] = merge(classes[c1], classes[c2])
                            classes.pop(c2)
        except:
            pass
    return cost



edges = []
edges_count = int(input("Введите кол-во ребер графа: "))
print("Вводите информацию о ребрах в следующем виде: ")
print("1 2 3")
print("где 1 и 2 - вершины, соединяемые ребром")
print("3 - вес ребра")
print("после каждой такой записи нажимайте enter")
for i in range(0, edges_count):
    edges.append([int(q) for q in input().split(" ")])

print("Результат работы алгоритма Крускала: "+str(kruskal(edges)))
