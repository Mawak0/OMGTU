


def Tau(mode, input_path=None, output_path=None):
    if mode == 'file':
        f = open(input_path, "r")
        phrase = f.read()
        f.close()
    if mode == "manual":
        phrase = input()


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
        out = Tau(mode="file", input_path="C:/Users/User/Downloads/Игра ~Города~/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Игра ~Города~/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Tau(mode="file", input_path="C:/Users/user/Downloads/Игра ~Города~/input_s1_04.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))