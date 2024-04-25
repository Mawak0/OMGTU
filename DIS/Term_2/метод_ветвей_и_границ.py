def ShowMatrix(matrix):
    for line in matrix:
        print(line)

def Delite(matrix, del_i, del_j):
    new_matrix = []
    for i in range(0, len(matrix)):
        if i != del_i:
            new_matrix.append([])
            for j in range(0, len(matrix)):
                if j != del_j:
                    new_matrix[-1].append(matrix[i][j])
    return new_matrix

def find_min(matrix):
    m_i = 0
    m_j = 0
    m_coords = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == 0:
                m_i = i
                m_j = j
                m_coords.append([m_i, m_j])
    return m_coords

def way_blocker(matrix, ways):
    new_matrix = []
    for i in range(0, len(matrix)):
        new_matrix.append(matrix[i][:])
    for way in ways:
        if (way[0] < len(matrix)) and (way[1] < len(matrix)):
            new_matrix[way[1]][way[0]] = inf
    t_ways = []
    old_len = -1
    while old_len != len(t_ways):
        old_len = len(t_ways)
        for w1 in ways:
            for w2 in ways:
                if w1 != w2:
                    if w1[1] == w2[0]:
                        if [w1[0], w2[1]] not in t_ways:
                            t_ways.append([w1[0], w2[1]])
    for way in t_ways:
        if (way[0] < len(matrix)) and (way[1] < len(matrix)):
           new_matrix[way[1]][way[0]] = inf

    return new_matrix
def Priv(matrix):
    w = 0
    for i in range(0, len(matrix)):
        m = matrix[i][0]
        for j in range(0, len(matrix)):
            if matrix[i][j] < m:
                m = matrix[i][j]
        if m != inf:
            for j in range(0, len(matrix)):
                matrix[i][j] = matrix[i][j] - m
            w += m
    for j in range(0, len(matrix)):
        m = inf
        for i in range(0, len(matrix)):
            m = min([m, matrix[i][j]])
        if m != inf:
            for i in range(0, len(matrix)):
                matrix[i][j] = matrix[i][j] - m
            w += m
    return [w, matrix]

inf = float("inf")
matrix = [ [ inf, 41, 17, 23, 32 ], [ 13, inf,  45, 12, 37 ], [ 80, 45, inf, 50, 64], [ 23, 12,50, inf, 67 ], [32, 37, 64, 67, inf ]]

old_matrix = [e[:] for e in matrix]

def build_chain(ways):
    chain = []
    used_points = []
    for w1 in ways:
        for w2 in ways:
            if w1 not in chain:
                if w2[1] not in used_points:
                    if len(chain) != 0:
                        if (chain[-1][1] == w1[0]) and (w1[1] == w2[0]):
                            chain.append(w1)
                            used_points.append(w1[1])
                            chain.append(w2)
                    else:
                        if (w1[1] == w2[0]):
                            chain.append(w1)
                            used_points.append(w1[1])
                            chain.append(w2)

    if len(chain) == len(ways):
        if old_matrix[chain[-1][1]][chain[0][0]] != inf:
            add_weight = old_matrix[chain[-1][1]][chain[0][0]]
            chain.append([chain[-1][1], chain[0][0]])
            return [chain, add_weight]

    return False



finals = []
record = inf

def work(pack):
    global record
    new_pack = []
    for p in pack:
        matrix = p[0]
        upper_plate = p[1]
        left_plate = p[2]
        ways = p[3]
        global_ways = p[4]
        weight = p[5]
        if upper_plate == None:
            upper_plate = [i for i in range(0, len(matrix))]
            left_plate = upper_plate[:]
            ways = []
            global_ways = []
            weight = 0
        if len(matrix) != 1:
            w, matrix = Priv(matrix)
            possible_del_coords = find_min(matrix)
            for coord in possible_del_coords:
                new_global_ways = [e[:] for e in global_ways]
                new_global_ways.append([left_plate[coord[0]], upper_plate[coord[1]]])
                new_weight = weight + old_matrix[new_global_ways[-1][0]][new_global_ways[-1][1]]
                if new_weight < record:
                    new_upper_plate = upper_plate[:]
                    new_left_plate = left_plate[:]
                    new_upper_plate.pop(coord[1])
                    new_left_plate.pop(coord[0])
                    new_ways = [e[:] for e in ways]
                    new_ways.append(coord)
                    new_matrix = [e[:] for e in matrix]
                    new_matrix = way_blocker(new_matrix, new_ways)
                    new_matrix = Delite(new_matrix, coord[0], coord[1])
                    new_pack.append([new_matrix, new_upper_plate, new_left_plate, new_ways, new_global_ways, new_weight])
        else:
            new_global_ways = [e[:] for e in global_ways]
            new_weight = weight
            good = True
            for way in new_global_ways:
                if (new_global_ways.count(way) > 1):
                    good = False
            if good:
                chain = build_chain(new_global_ways)
                if chain:
                    solution = [new_weight + chain[1], chain[0]]
                    if solution[0] < record:
                        record = solution[0]
                        finals.append(solution)
        if len(new_pack) != 0:
            work(new_pack)

first_pack = [[matrix, None, None, None, None, None]]
work(first_pack)

finals.sort()
for i in range(0, len(finals[0][1])):
    finals[0][1][i][0] = finals[0][1][i][0]+1
    finals[0][1][i][1] = finals[0][1][i][1]+1
print(finals[0])
