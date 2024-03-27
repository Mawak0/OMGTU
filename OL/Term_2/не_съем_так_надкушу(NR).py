


def Prog(mode, input_path=None, output_path=None):
    if mode == 'file':
        f = open(input_path, "r")
        N, M = [int(i) for i in f.readline().strip().split(" ")]
        branches = []
        for i in range(0, N):
            branches.append([int(q) for q in f.readline().strip().split(" ")])
        apples = []
        for i in range(0, M):
            apples.append([int(q) for q in f.readline().strip().split(" ")])
        X, Z = [int(q) for q in f.readline().strip().split(" ")]
        f.close()
    if mode == "manual":
        N, M = [int(i) for i in input().split(" ")]
        branches = []
        for i in range(0, N):
            branches.append([int(q) for q in input().split(" ")])
        apples = []
        for i in range(0, M):
            apples.append([int(q) for q in input().split(" ")])
        X, Z = [int(q) for q in input().strip().split(" ")]



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
        out = Prog(mode="file", input_path="C:/Users/User/Downloads/Игра ~Города~/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Игра ~Города~/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Prog(mode="file", input_path="C:/Users/user/Downloads/Игра ~Города~/input_s1_04.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))