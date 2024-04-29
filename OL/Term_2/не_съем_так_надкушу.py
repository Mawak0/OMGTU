


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


    new_apples = []
    for a in apples:
        if a[1] >= Z:
            new_apples.append(a)
    apples = new_apples

    bra = dict()
    old_len = -1
    while old_len != len(bra):
        old_len = len(bra)
        for b in range(0, len(branches)):
            need = False
            if X-1 == b:
                need = True
            for a in apples:
                if a[0]-1 == b:
                    need = True
            for br in branches:
                if br[0]-1 == b:
                    need = True
            if need:
                bra[b+1] = branches[b]
    branches = bra
    def find_apples_routes():
        routes = []
        for a in apples:
            routes.append([])
            p = a[0]-1
            while p != -1:
                routes[-1].append({p+1: branches[p+1]})
                p = branches[p+1][0]-1
        return routes

    def find_worm_route():
        route = []
        p = X - 1
        while p != -1:
            route.append({p + 1: branches[p + 1]})
            p = branches[p + 1][0] - 1
        return route


    used_branches = [0, []]
    def find_max_route():
        worm_route = find_worm_route()
        apple_routes = find_apples_routes()
        routes = []

        for e in apple_routes:
            routes.append([])
            for r in worm_route:
                routes[-1].append(r)
            for ee in e:
                if ee not in routes[-1]:
                    routes[-1].append(ee)
                else:
                    routes[-1].remove(ee)
        max_route_length = 0
        for route in routes:
            sum = 0
            for e in route:
                for key, value in e.items():
                    if e not in used_branches[1]:
                        used_branches[1].append(e)
                        used_branches[0] = used_branches[0] + value[1]
                    sum += value[1]
            max_route_length = max(max_route_length, sum)
        return max_route_length


    if find_max_route() == 0:
        out_str = "0"
    else:
        out_str = str(used_branches[0]*2 - find_max_route())

    if mode == 'auto':
        f = open(output_path, "w")
        f.write(out_str)
        f.close()
    return out_str





autocheck = True

if autocheck:
    for w in range(1, 26):
        q = str(w)
        if len(q) == 1:
            q = "0" +q
        print(q)
        out = Prog(mode="file", input_path="C:/Users/user/Downloads/Не съем, так надкушу/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Не съем, так надкушу/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Prog(mode="file", input_path="C:/Users/user/Downloads/Не съем, так надкушу/input_s1_20.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))
