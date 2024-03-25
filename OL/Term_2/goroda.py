








def Goroda(mode, input_path=None, output_path=None):
    
    def have_alone(mass):
        for e in mass:
            if len(e) == 1:
                return e[0]
        return False
        
    def is_ring(chain):
        if chain[0][0] == chain[-1][-1]:
            return True
        
        return False
    
    def Show_chains(chains):
        print("----------------------")
        for line in chains:
            print(line)
            print("---------------------")
    
    words = []
    if mode == 'auto':
        f = open(input_path, "r")
        words = [l.strip() for l in f.readlines()]
    if mode == "manual":
        n = int(input())
        for i in range(0, n):
            words.append(input())
    for i in range(0, len(words)):
        words[i] = words[i][0]+words[i][-1]
    print(words)
    chains = [] #[random, good]
    for i in range(0, len(words)):
        added = False
        if words[i] != "":
            for ch_i in range(0, len(chains)):
                if not added:
                    #print(chains)
                    #print(words[i])
                    if chains[ch_i][0][-1][-1] == words[i][0]:
                        
                        chains[ch_i][0].append(words[i])
                        if is_ring(chains[ch_i][0]):
                            chains[ch_i][1] = chains[ch_i][0][:]
                        #words[i] = ""
                        added = True
            if not added:
                chains.append([[words[i]], [words[i]]])
    # while have_alone(chains):
    #     word = have_alone(chains)
    #     solved = False
    #     for ch_i in range(0, len(chains)):
    #         for ch_word_i in range(0, len(chains[ch_i])):
    #             if chains[ch_i][ch_word_i][-1] == word[0]:
    #                 chains[ch_i].insert(ch_word_i+1, word)
    #                 chains.remove([word])
    #                 solved = True
    #                 break
    #         if solved:
    #             break
    
    
    пытаемся каждую цепочку запихнуть в другую цепочку
    
    new_ringed_chains = []
    def inserts(ch_from):
        for ch_to in range(0, len(chains)):
            for ch_word_i in range(0, len(chains[ch_to][1])):
                if chains[ch_from][1][0][0] == chains[ch_to][1][ch_word_i][-1]:
                    if chains[ch_from][1][-1][-1] == chains[ch_to][1][ch_word_i+len(chains[ch_to][1])][0]:
                        #chains[ch_i].insert(ch_word_i+1, word)
                        #chains.remove([word])
                        to_app = []
                        for i in range(0, len(chains[ch_to][1])+len(chains[ch_from][1])):
                            if i <= ch_word_i:
                                to_app.append(chains[ch_to][1][i])
                            elif i <= ch_word_i+len(chains[ch_to][1]):
                                to_app.append(chains[ch_from][1][i-ch_word_i])
                            else:
                                to_app.append(chains[ch_to][1][i-ch_word_i])
                        new_ringed_chains.append(to_app)
                        return
    for ch_from in range(0, len(chains)):
        inserts(ch_from)
    
    Show_chains(chains)
    # FINE = True
    # for ch_i in range(0, len(chains)):
    #     if not is_ring(chains[ch_i]):
    #         FINE = False
    #         print("ПОЛНЫЙ КАПЕЦ")
    #         print(chains[ch_i])
    #         w = 0
    #         while not is_ring(chains[ch_i]):
    #             if (w % 2 == 0):
    #                 chains.append([chains[ch_i].pop(-1)])
    #             else:
    #                 chains.append([chains[ch_i].pop(0)])
    #             w += 1
    #         print("ИСПРАВЛЕНО")
                
    
    if mode == 'auto':
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
    #print(Goroda("C:/Users/User1/Downloads/Игра ~Города~/input_s1_01.txt", "output.txt", "auto"))
    print(Goroda(mode='manual'))
    
