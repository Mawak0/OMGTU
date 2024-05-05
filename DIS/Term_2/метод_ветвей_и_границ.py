def ShowMatrix(matrix):
    print("-----------------")
    for line in matrix:
        print(line)
    print("-----------------")


def Priv(matrix):
    for i in range(0, len(matrix)):
        m = min(matrix[i])
        if m != inf:
            for j in range(0, len(matrix)):
                matrix[i][j] = matrix[i][j] - m
    for j in range(0, len(matrix)):
        m = inf
        for i in range(0, len(matrix)):
            m = min([m, matrix[i][j]])
        if m != inf:
            for i in range(0, len(matrix)):
                matrix[i][j] = matrix[i][j] - m
    return matrix

def Delite(matrix, del_i, del_j):
    new_matrix = []
    for i in range(0, len(matrix)):
        if i != del_i:
            new_matrix.append([])
            for j in range(0, len(matrix)):
                if j != del_j:
                    new_matrix[-1].append(matrix[i][j])
    return new_matrix


def build_chain(ways):
    ways.sort()
    chain = []
    used_points = []
    for w1 in ways:
        for w2 in ways:
            if w2[1] not in used_points:
                if len(chain) != 0:
                    if (chain[-1][1] == w1[0]) and (w1[1] == w2[0]):
                        if w1 not in chain:
                            chain.append(w1)
                        used_points.append(w1[1])
                        chain.append(w2)
                    elif (chain[-1][1] == w2[0]):
                        used_points.append(w2[0])
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
    else:
        chain2 = []
        for w1 in ways:
            for w2 in ways:
                if w1 not in chain and w1 not in chain2:
                    if w2[1] not in used_points:
                        if len(chain2) != 0:
                            if (chain2[-1][1] == w1[0]) and (w1[1] == w2[0]):
                                chain2.append(w1)
                                used_points.append(w1[1])
                                chain2.append(w2)
                        else:
                            if (w1[1] == w2[0]):
                                chain2.append(w1)
                                used_points.append(w1[1])
                                chain2.append(w2)


        for w1 in ways:
            if w1 not in chain and w1 not in chain2:
                chain2.append(w1)

        add_weight = 0
        if chain[-1][1] != chain2[0][0]:
            if old_matrix[chain[-1][1]][chain2[0][0]] != inf:
                add_weight += old_matrix[chain[-1][1]][chain2[0][0]]
                chain.append([chain[-1][1], chain2[0][0]])
        for w in chain2:
            chain.append(w)


        if old_matrix[chain[-1][1]][chain[0][0]] != inf:
            add_weight += old_matrix[chain[-1][1]][chain[0][0]]
            chain.append([chain[-1][1], chain[0][0]])


    return [chain, add_weight]



def find_max(matrix, left_plate, upper_plate):
    zeros = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == 0:
                #print([left_plate[i], upper_plate[j]])
                cop_m = [e[:] for e in matrix]
                cop_m[i][j] = inf

                const_sum = min(cop_m[i])
                min_e = inf
                for ii in range(0, len(matrix)):
                    min_e = min([min_e, cop_m[ii][j]])
                const_sum += min_e
                if const_sum != inf:
                    #print("blocked_ways "+str(blocked_ways))
                    if [left_plate[i], upper_plate[j]] not in blocked_ways:
                        zeros.append([const_sum, [i, j]])
    zeros.sort()
    return zeros



inf = float("inf")
matrix = [ [ inf, 41, 17, 23, 32 ], [ 13, inf,  45, 12, 37 ], [ 80, 45, inf, 50, 64], [ 23, 12,50, inf, 67 ], [32, 37, 64, 67, inf ]]
#matrix = [ [ inf, 41, 17, 23, 32, 20 ], [ 13, inf,  45, 12, 37, 20 ], [ 80, 45, inf, 50, 64, 20], [ 23, 12,50, inf, 67, 20 ], [32, 37, 64, 67, inf, 20 ], [32, 37, 64, 67, 20, inf ]]

old_matrix = [e[:] for e in matrix]



record = inf
blocked_ways = []

def work():
    global matrix
    way = []
    upper_plate = [i for i in range(1, len(matrix)+1)]
    left_plate = upper_plate[:]
    while len(matrix) != 1:
        t_ways = []
        old_len = -1
        while old_len != len(t_ways):
            old_len = len(t_ways)
            for w1 in way:
                for w2 in way:
                    if w1 != w2:
                        if w1[1] == w2[0]:
                            if [w1[0], w2[1]] not in t_ways:
                                t_ways.append([w1[0], w2[1]])
            for w1 in t_ways:
                for w2 in way:
                    if w1 != w2:
                        if w1[1] == w2[0]:
                            if [w1[0], w2[1]] not in t_ways:
                                t_ways.append([w1[0], w2[1]])
        for w in t_ways:
            blocked_ways.append(w[::-1])
            try:
                matrix[w[1]][w[0]] = inf
            except:
                pass
        matrix = Priv(matrix)
        v = find_max(matrix, left_plate, upper_plate)
        if len(v) != 0:
            v = v[-1]
            blocked_ways.append([upper_plate[v[1][1]], left_plate[v[1][0]]])
            matrix[v[1][1]][v[1][0]] = inf
            way.append([left_plate.pop(v[1][0]), upper_plate.pop(v[1][1])])
            matrix = Delite(matrix, v[1][0], v[1][1])
        else:
            break
    # for i in range(0, len(matrix)):
    #     for j in range(0, len(matrix)):
    #         if matrix[i][j] != inf:
    #             way.append([left_plate.pop(i), upper_plate.pop(j)])
    q_w = []
    for w in way:
        q_w.append([w[0]-1, w[1]-1])
    weight = 0
    for w in way:
        weight += old_matrix[w[0]-1][w[1]-1]
    chain, add_weight = build_chain(q_w)
    new_chain = []
    for c in chain:
        new_chain.append([c[0]+1, c[1]+1])
    print(new_chain, weight+add_weight)

work()


