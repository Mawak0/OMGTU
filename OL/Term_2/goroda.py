
def Goroda(mode, input_path=None, output_path=None):

    def find_doubles(string):
        doubles = set()
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                doubles.add(string[i:i + 2])
        return doubles

    def rotate_palindrome(string, index):
        left = string[:index]
        right = string[index:]
        return right + left


    words = []
    if mode == 'file':
        f = open(input_path, "r")
        words = [l.strip() for l in f.readlines()]
    if mode == "manual":
        n = int(input())
        for i in range(0, n):
            words.append(input())
    for i in range(0, len(words)):
        words[i] = words[i][0 ] +words[i][-1]
    #print(words)
    chains = [0 for i in range(0, len(words))]
    action_global = True
    while action_global == True:
        action_global = False
        for i in range(0, len(words)):
            action = True
            while action == True:
                action = False
                if words[i] != "":
                    for w in range(0, len(words)):
                        if words[w] != "":
                            if (w != i) and (words[i][-1] == words[w][0]):
                                words[i] = words[i]+words[w]
                                words[w] = ""
                                chains[i] = chains[i] + 1 + chains[w]
                                action = True
                                action_global = True
                                continue
                            if (w != i) and (words[w][-1] == words[i][0]):
                                words[i] = words[w]+words[i]
                                words[w] = ""
                                chains[i] = chains[i] + 1 + chains[w]
                                action = True
                                action_global = True
                                continue
                            if ((len(words[i]) > 2) and (len(words[w]) > 2) and (i != w)):
                                doubles_in_i = find_doubles(words[i])
                                for d in doubles_in_i:
                                    if d in words[w]:
                                        words[w] = rotate_palindrome(words[w], words[w].find(d)+1)
                                        break

                    for w in range(0, len(words)):
                        if words[w] != "":
                            if ((len(words[i]) > 2) and (len(words[w]) > 2) and (i != w) and (words[w][0]+words[w][-1] in words[i])):
                                pos = words[i].find(words[w][0]+words[w][-1])
                                words[i] = words[i][:pos]+words[w]+words[i][pos:]
                                break





    chains = [c+1 for c in chains]
    out = []
    #print(words)
    #print(chains)
    for i in range(0, len(words)):
        if words[i] != '':
            out.append(chains[i])
    out_str = str(len(out))
    out.sort(reverse=True)
    for e in out:
        out_str = out_str+"\n"+str(e)

    if mode == 'auto':
        f = open(output_path, "w")
        f.write(out_str)
        f.close()
    return out_str


autocheck = True

if autocheck:
    for w in range(1, 14):
        q = str(w)
        if len(q) == 1:
            q = "0" +q
        print(q)
        out = Goroda(mode="file", input_path="C:/Users/User/Downloads/Игра ~Города~/input_s1_"+q+".txt", output_path="output.txt")
        f = open("C:/Users/User/Downloads/Игра ~Города~/output_s1_" + q +".txt")
        u = f.read()
        if out != u:
            print("ERROR")
            print(u)
            print("-----------")
            print(out)

else:
    print(Goroda(mode="file", input_path="C:/Users/user/Downloads/Игра ~Города~/input_s1_04.txt", output_path="output.txt"))
    # print(Goroda(mode='manual'))

