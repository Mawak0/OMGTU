
def matrix_multiplication(matrix, vector):
    res = []
    for j in range(0, 3):
        sum = 0
        for i in range(0, 3):
            sum += matrix[j][i]*vector[i]
        res.append(sum)
    return res


def Work(mode, input_path=None, output_path=None):
    rotation = []
    N = 0
    M = 0


    x_po = [
        [1, 0, 0],
        [0, 0, 1],
        [0, -1, 0]
    ]
    x_pr = [
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]
    ]
    y_pr = [
        [0, 0, -1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    y_po = [
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0]
    ]
    z_po = [
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1]
    ]
    z_pr = [
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ]


    if mode == 'file':
        f = open(input_path, "r")
        N, M = [int(i) for i in f.readline().strip().split(" ")]
        XN, YN, ZN = [int(i) for i in f.readline().strip().split(" ")]
        for i in range(0, M):
            rotation.append([q for q in f.readline().strip().split(" ")])
            rotation[-1][1] = int(rotation[-1][1])
            rotation[-1][2] = int(rotation[-1][2])
        f.close()
    if mode == "manual":
        N, M = [int(i) for i in input().split(" ")]
        XN, YN, ZN = [int(i) for i in input().split(" ")]
        for i in range(0, M):
            rotation.append([q for q in input().strip().split(" ")])
            rotation[-1][1] = int(rotation[-1][1])
            rotation[-1][2] = int(rotation[-1][2])

    for r in rotation:

        new_x = XN - (N+1)/2
        new_y = YN - (N+1)/2
        new_z = ZN - (N+1)/2
        vec = [new_x, new_y, new_z]

        new_vec = vec[:]
        if r[0] == "X":
            if XN == r[1]:
                if r[2] == 1:
                    new_vec = matrix_multiplication(x_po, vec)
                if  r[2] == -1:
                    new_vec = matrix_multiplication(x_pr, vec)
        elif r[0] == "Y":
            if YN == r[1]:
                if r[2] == 1:
                    new_vec = matrix_multiplication(y_po, vec)
                if  r[2] == -1:
                    new_vec = matrix_multiplication(y_pr, vec)
        elif r[0] == "Z":
            if ZN == r[1]:
                if r[2] == 1:
                    new_vec = matrix_multiplication(z_po, vec)
                if  r[2] == -1:

                    new_vec = matrix_multiplication(z_pr, vec)

        vec = new_vec[:]
        XN = vec[0] +  (N + 1) / 2
        YN = vec[1] + (N + 1) / 2
        ZN = vec[2] + (N + 1) / 2

    out_str = str(int(XN))+" "+str(int(YN))+" "+str(int(ZN))

    if mode == 'auto':
        f = open(output_path, "w")
        f.write(out_str)
        f.close()
    return out_str





autocheck = True

if autocheck:
    for w in range(1, 21):
        q = str(w)
        if len(q) == 1:
            q = "0" +q
        print(q)
        out = Work(mode="file", input_path="C:/Users/User/Downloads/Кубик Рубика/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Кубик Рубика/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Work(mode="file", input_path="C:/Users/User/Downloads/Кубик Рубика/input_s1_01.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))
