

def Goroda(input_path, output_path):


    f = open(input_path, "r")
    words = [l.strip() for l in f.readlines()]
    for i in range(0, len(words)):
        words[i] = words[i][0]+words[i][-1]
    print(words)
    chains = []
    for i in range(0, len(words)):
        added = False
        if words[i] != "":
            for ch_i in range(0, len(chains)):
                if chains[ch_i][-1][-1] == words[i][0]:
                    chains[ch_i].append(words[i])
                    words[i] = ""
                    added = True
            


    f = open(output_path, "w")
    f.write(str())
    f.close()
    return


autocheck = False

if autocheck:
    for w in range(1, 14):
        q = str(w)
        if len(q) == 1:
            q = "0"+q
        print(q)
        out = Goroda("C:/Users/User1/Downloads/Игра ~Города~/input_s1_"+q+".txt", "output.txt")
        f = open("C:/Users/User1/Downloads/Игра ~Города~/output_s1_"+q+".txt")
        u = f.readline().strip()
        if out != int(u):
            print("ERROR")

else:
    print(Goroda("C:/Users/User1/Downloads/Игра ~Города~/input_s1_01.txt", "output.txt"))
