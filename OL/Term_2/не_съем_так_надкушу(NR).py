


def Prog(mode, input_path=None, output_path=None):
    apples = []
    branches = []
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
        for i in range(0, N):
            branches.append([int(q) for q in input().split(" ")])

        for i in range(0, M):
            apples.append([int(q) for q in input().split(" ")])
        X, Z = [int(q) for q in input().strip().split(" ")]


    for a in apples:
        if a[1] < Z:
            apples.remove(a)
    print(apples)
    bra = dict()
    print(branches)
    new_branches= []
    old_len = -1
    while old_len != len(new_branches):
        old_len = len(new_branches)
        for b in range(0, len(branches)):
            need = False
            for a in apples:
                if a[0]-1 == b:
                    need = True
            for br in branches:
                if br[0]-1 == b:
                    need = True

            bra[str(b)] = branches[b]
    print(new_branches)
    print(bra)
    branches = new_branches

    def find_routes():
        routes = []
        for a in apples:
            routes.append([])
            p = a[0]-1
            while p != -1:
                print(a)
                print(p)
                routes[-1].append(branches[p])
                p = branches[p][0]-1
        print(routes)
    find_routes()

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
        out = Prog(mode="file", input_path="C:/Users/User/Downloads/Не съем, так надкушу/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Не съем, так надкушу/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Prog(mode="file", input_path="C:/Users/User/Downloads/Не съем, так надкушу/input_s1_01.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))
