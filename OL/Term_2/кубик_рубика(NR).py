


def Cube(mode, input_path=None, output_path=None):
    if mode == 'file':
        f = open(input_path, "r")
        N, M = [int(i) for i in f.readline().strip().split(" ")]
        XN, YN, ZN = [int(i) for i in f.readline().strip().split(" ")]
        rotation = []
        for i in range(0, M):
            rotation.append([int(q) for q in f.readline().strip().split(" ")])
        f.close()
    if mode == "manual":
        N, M = [int(i) for i in input().split(" ")]
        XN, YN, ZN = [int(i) for i in input().split(" ")]
        rotation = []
        for i in range(0, M):
            rotation.append([int(q) for q in input().split(" ")])



    out_str = ""


    if mode == 'auto':
        f = open(output_path, "w")
        f.write(out_str)
        f.close()
    return out_str





autocheck = False

if autocheck:
    for w in range(1, 14):
        q = str(w)
        if len(q) == 1:
            q = "0" +q
        print(q)
        out = Cube(mode="file", input_path="C:/Users/User/Downloads/Игра ~Города~/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Игра ~Города~/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Cube(mode="file", input_path="C:/Users/user/Downloads/Игра ~Города~/input_s1_04.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))