


def Prog(mode, input_path=None, output_path=None):
    if mode == 'file':
        f = open(input_path, "r")
        N = int(f.readline().strip())
        actions = []
        for i in range(0, N):
            actions.append(f.readline().strip().split(" "))
        R = int(f.readline().strip())
        f.close()
    if mode == "manual":
        N = int(input().strip())
        actions = []
        for i in range(0, N):
            actions.append(input().strip().split(" "))
        R = int(input().strip())



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