
def Show_matr(matr):
    print("--------------------")
    for line in matr:
        print(line)
    print("--------------------")


def WaveAlg(matr):
    inf = float("inf")

    def build_backway(matr, finish, pos):
        def find_nearest_point():
            way1 = matr[pos[0]+1][pos[1]]
            way2 = matr[pos[0]-1][pos[1]]
            way3 = matr[pos[0]+1][pos[1]+1]
            way4 = matr[pos[0]+1][pos[1]-1]
            way5 = matr[pos[0]-1][pos[1]+1]
            way6 = matr[pos[0]-1][pos[1]-1]
            way7 = matr[pos[0]][pos[1]+1]
            way8 = matr[pos[0]][pos[1]-1]
            if way1 == c:
                return [pos[0]+1, pos[1]]
            if way2 == c:
                return [pos[0]-1, pos[1]]
            if way3 == c:
                return [pos[0]+1, pos[1]+1]
            if way4 == c:
                return [pos[0]+1, pos[1]-1]
            if way5 == c:
                return [pos[0]-1, pos[1]+1]
            if way6 == c:
                return [pos[0]-1, pos[1]-1]
            if way7 == c:
                return [pos[0], pos[1]+1]
            if way8 == c:
                return [pos[0], pos[1]-1]

        c = matr[finish[0]][finish[1]]
        notebook = []
        while c != 0:
            c -= 1
            pos = find_nearest_point()
            notebook.append(pos)
        return notebook

    def go_right(pos, matr):
        new_pos = [pos[0], pos[1]+1]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_left(pos, matr):
        new_pos = [pos[0], pos[1]-1]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_up(pos, matr):
        new_pos = [pos[0]-1, pos[1]]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_down(pos, matr):
        new_pos = [pos[0]+1, pos[1]]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_right_up(pos, matr):
        new_pos = [pos[0]-1, pos[1]+1]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_right_down(pos, matr):
        new_pos = [pos[0]+1, pos[1]+1]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_left_up(pos, matr):
        new_pos = [pos[0]-1, pos[1]-1]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr
    def go_left_down(pos, matr):
        new_pos = [pos[0]+1, pos[1]-1]
        if matr[new_pos[0]][new_pos[1]] == inf:
            matr[new_pos[0]][new_pos[1]] = matr[pos[0]][pos[1]]+1
        return matr

    def get_current_pos(matr, c):
        pos_m = []
        for i in range(0 , len(matr)):
            for j in range(0, len(matr[0])):
                if matr[i][j] == c:
                    pos_m.append([i, j])
        return pos_m

    c = 0
    while c!= len(matr)*len(matr[0]):
        pos_m = get_current_pos(matr, c)
        for pos in pos_m:
            go_right(pos, matr)
            go_left(pos, matr)
            go_up(pos, matr)
            go_down(pos, matr)
            go_left_down(pos, matr)
            go_left_up(pos, matr)
            go_right_down(pos, matr)
            go_right_up(pos, matr)
        c += 1
    if matr[finish[0]][finish[1]] != inf:
        Show_matr(matr)
        print(build_backway(matr, finish, finish))

    else:
        print("нет пути")




w = -1
i = float("inf")
finish = [11,7]
matr = [
    [w,w,w,w,w,w,w,w,w],
    [w,i,i,i,i,i,i,i,w],
    [w,i,i,i,i,w,i,i,w],
    [w,i,i,w,i,w,i,i,w],
    [w,0,i,w,i,w,i,i,w],
    [w,i,i,w,i,i,i,i,w],
    [w,i,i,w,i,i,i,i,w],
    [w,i,i,i,i,i,i,i,w],
    [w,i,i,i,i,w,w,w,w],
    [w,i,w,i,i,i,i,i,w],
    [w,i,w,i,i,i,i,i,w],
    [w,i,w,i,i,i,i,i,w],
    [w,w,w,w,w,w,w,w,w]
]
WaveAlg(matr)
