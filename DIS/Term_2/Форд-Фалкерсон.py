
def Show_weigth_matrix(weigth_matrix):
    print("--------------------")
    for line in weigth_matrix:
        print(line)
    print("--------------------")

def able_to_go(point, dead_points):
    able = []
    for j in range(0, len(weigth_matrix)):
        if j not in dead_points:
            if (weigth_matrix[point][j] != inf) and (weigth_matrix[point][j][0] != 0):
                able.append([j, weigth_matrix[point][j][0]])
    def s(i):
        return i[1]
    able.sort(key=s)
    able.reverse()
    return able

def able_to_reverse(point):
    able_rev = []
    for i in range(0, len(weigth_matrix)):
        if weigth_matrix[i][point][1] != 0:
            able_rev.append([i, weigth_matrix[i][point][1]])
    return able_rev

def FF():
    while True:
        current_point = start
        way = [current_point]
        dead_points = []
        marks = [] #[point, flow, from]
        while current_point != finish:
            able = able_to_go(current_point, dead_points)
            if len(able) == 0:
                if current_point == start:
                    print("итс овер")
                else:
                    dead_points.append(current_point)
                    if len(able_to_go(way[-2], dead_points)) != 0:
                        way.pop(-1)
                        current_point = way[-1]
                    else:
                        dead_points.remove(current_point)
                        able_rev = able_to_reverse(current_point)
                        backway = able_rev[0]
                        way.append(backway[0])
                        flow = backway[1]
                        weigth_matrix[backway[0]][current_point][0] = weigth_matrix[backway[0]][current_point][0] + flow
                        weigth_matrix[backway[0]][current_point][1] = weigth_matrix[backway[0]][current_point][1] - flow
                        #marks.append([backway[0], flow, current_point])
                        continue


            next_point, flow = able[0]
            marks.append([next_point, flow, current_point])
            way.append(next_point)
            current_point = next_point
        min_flow = inf
        for m in marks:
            min_flow = min([min_flow, m[1]])
        old_w = way[0]
        for i in range(1, len(way)):
            weigth_matrix[old_w][way[i]][0] = weigth_matrix[old_w][way[i]][0] - min_flow
            weigth_matrix[old_w][way[i]][1] = weigth_matrix[old_w][way[i]][1] + min_flow
            old_w = way[i]

        Show_weigth_matrix(weigth_matrix)
        #print(current_used_flow)
        print(marks)
        input()









edges = []
edges_count = int(input("Введите кол-во дуг графа: "))
print("Вводите информацию о дугах в следующем виде: ")
print("1 2 3")
print("где 1 и 2 - вершины, соединяемые дугой")
print("3 - пропускная способность")
print("после каждой такой записи нажимайте enter")

inf = float("inf")

for i in range(0, edges_count):
    edges.append([int(q) for q in input().split(" ")])

points = set()
for e in edges:
    points.add(e[0])
    points.add(e[1])

weigth_matrix = []

for p in range(0, len(points ) +1):
    weigth_matrix.append([[0, 0] for i in range(0, len(points ) +1)])


for e in edges:
    weigth_matrix[e[0]][e[1]] = [e[2], 0] #max/used
Show_weigth_matrix(weigth_matrix)

start = int(input("Введите точку истока: "))
finish = int(input("Введите точку стока: "))
FF()
