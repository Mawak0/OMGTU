


def Prog(mode, input_path=None, output_path=None):
    gears = []
    connections = []
    if mode == 'file':
        f = open(input_path, "r")
        N, M = [int(q) for q in f.readline().strip().split(" ")]
        for i in range(0, N):
            gears.append([int(q) for q in f.readline().strip().split(" ")])
        for i in range(0, M):
            connections.append([int(q)-1 for q in f.readline().strip().split(" ")])
        Z1, Z2 = [int(q)-1 for q in f.readline().strip().split(" ")]
        V = int(f.readline().strip())
        f.close()
    else:
        N, M = [int(q) for q in input().split(" ")]
        for i in range(0, N):
            gears.append([int(q) for q in input().split(" ")])
        for i in range(0, M):
            connections.append([int(q)-1 for q in input().split(" ")])
        Z1, Z2 = [int(q)-1 for q in input().split(" ")]
        V = int(input())
    gears.sort()
    connections.sort()
    gears[Z1].append(V)
    for i in range(0, len(gears)):
        if i != Z1:
            gears[i].append(0)
    def sig(a):
        if a > 0:
            return 1
        if a < 0:
            return -1
        else:
            return 0


    for i in range(0, len(connections)):
        if (gears[connections[i][0]][2] != 0) and (gears[connections[i][1]][2] == 0):
            diff = gears[connections[i][0]][1] / gears[connections[i][1]][1]
            gears[connections[i][1]][2] = - gears[connections[i][0]][2]*diff

        elif (gears[connections[i][0]][2] == 0) and (gears[connections[i][1]][2] != 0):
            diff = gears[connections[i][1]][1] / gears[connections[i][0]][1]
            gears[connections[i][0]][2] = - gears[connections[i][1]][2] * diff

        elif (gears[connections[i][0]][2] != 0) and (gears[connections[i][1]][2] != 0):
            if sig(gears[connections[i][0]][2]) == sig(gears[connections[i][1]][2]):
                gears[Z2][2] = 0
                break


    if gears[Z2][2] != 0:
        q = str(abs(round(gears[Z2][2], 3)))

        while len(q.split(".")[1]) < 3:
            q = q + "0"

        out_str = "1\n"+str(sig(gears[Z2][2]))+"\n"+q
    else:
        out_str = "-1"


    if mode == 'auto':
        f = open(output_path, "w")
        f.write(out_str)
        f.close()
    return out_str





print(Prog(mode="file", input_path="C:/Users/User/Downloads/Шестренки/input_s1_08.txt", output_path="output.txt"))
