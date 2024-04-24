
class Cube:
    forward = []
    backward = []
    upper = []
    lower = []
    right = []
    left = []
    N = 0
    def __init__(self, N):
        self.forward = [[0 for i in range(0, N)] for w in range(0, N)]
        self.backward = [[0 for i in range(0, N)] for w in range(0, N)]
        self.upper = [[0 for i in range(0, N)] for w in range(0, N)]
        self.lower = [[0 for i in range(0, N)] for w in range(0, N)]
        self.right = [[0 for i in range(0, N)] for w in range(0, N)]
        self.left = [[0 for i in range(0, N)] for w in range(0, N)]
        self.N = N-1
    def set_elem(self, X, Y, Z):
        if Y == 0:
            self.forward[Z][X] = 1
        if X == self.N:
            self.right[Z][Y] = 1
        if Y == self.N:
            self.backward[Z][self.N - X] = 1
        if X == 0:
            self.left[Z][self.N-Y] = 1
        if Z == 0:
            self.lower[self.N-Y][X] = 1
        if Z == self.N:
            self.upper[Y][X] = 1

    def locate_elem(self): # X Y Z
        N = self.N
        coords = []
        for i in range(0, N+1):
            for j in range(0, N+1):
                if self.forward[i][j] == 1:
                    coords.append([j, 0, i])
                if self.backward[i][j] == 1:
                    coords.append([N-j, N, i])
                if self.upper[i][j] == 1:
                    coords.append([j, i, N])
                if self.lower[i][j] == 1:
                    coords.append([j, N-i, 0])
                if self.right[i][j] == 1:
                    coords.append([N, j, i])
                if self.left[i][j] == 1:
                    coords.append([0, N-j, i])
        print(coords)
        return coords[0]
    def rotate(self, axis, k, count):
        k = k-1
        if axis == "X":
            if self.locate_elem()[0] != k:
                return
        if axis == "Y":
            if self.locate_elem()[1] != k:
                return
        if axis == "Z":
            if self.locate_elem()[2] != k:
                return

        for c in range(0, count):
            N = self.N+1
            new_forward = [[0 for i in range(0, N)] for w in range(0, N)]
            new_backward = [[0 for i in range(0, N)] for w in range(0, N)]
            new_right = [[0 for i in range(0, N)] for w in range(0, N)]
            new_left = [[0 for i in range(0, N)] for w in range(0, N)]
            new_upper = [[0 for i in range(0, N)] for w in range(0, N)]
            new_lower = [[0 for i in range(0, N)] for w in range(0, N)]
            if axis == "Z":
                new_forward[k] = self.right[k]
                new_right[k] = self.backward[k]
                new_backward[k] = self.left[k]
                new_left[k] = self.forward[k]
            if axis == "Y":
                for i in range(0, self.N+1):
                    new_upper[k][i] = self.left[i][self.N-k]
                    new_left[i][self.N-k] = self.lower[self.N-k][self.N-i]
                    new_lower[self.N-k][i] = self.right[i][k]
                    new_right[i][k] = self.upper[k][self.N-i]
            if axis == "X":
                for i in range(0, self.N+1):
                    new_lower[i][k] = self.backward[self.N-i][self.N-k]
                    new_backward[i][self.N-k] = self.upper[self.N-i][k]
                    new_upper[i][k] = self.forward[i][k]
                    new_forward[i][k] = self.lower[i][k]



            self.upper = new_upper
            self.lower = new_lower
            self.forward = new_forward
            self.right = new_right
            self.left = new_left
            self.backward = new_backward
            self.set_elem(*self.locate_elem())
    def show(self):
        print(self.forward)
        print(self.backward)
        print(self.left)
        print(self.right)
        print(self.upper)
        print(self.lower)




def Work(mode, input_path=None, output_path=None):
    rotation = []
    N = 0
    M = 0
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

    out_str = ""
    while N != 1:
        cube = Cube(N)
        cube.set_elem(XN-1, YN-1, ZN-1)
        cube.show()
        try:
            print(cube.locate_elem())
            for r in rotation:
                if r[2] == -1:
                    cube.rotate(r[0], r[1], 3)
                else:
                    cube.rotate(r[0], r[1], 1)

            coords = [i + 1 for i in cube.locate_elem()]
            out_str = str(coords[0]) + " " + str(coords[1]) + " " + str(coords[2])
            break
        except:
            N = N-1
            XN -= 1
            YN -= 1
            ZN -= 1
            for i in range(0, M):
                if rotation[i][1] != 1:
                    rotation[i][1] = rotation[i][1] - 1
                else:
                    rotation.pop(i)
        if out_str == "":
            out_str = str(XN)+" "+str(YN)+" "+str(ZN)



    if mode == 'auto':
        f = open(output_path, "w")
        f.write(out_str)
        f.close()
    return out_str





autocheck = False

if autocheck:
    for w in range(1, 21):
        q = str(w)
        if len(q) == 1:
            q = "0" +q
        print(q)
        out = Work(mode="file", input_path="C:/Users/user/Downloads/Кубик Рубика/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/user/Downloads/Кубик Рубика/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Work(mode="file", input_path="C:/Users/user/Downloads/Кубик Рубика/input_s1_11.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))