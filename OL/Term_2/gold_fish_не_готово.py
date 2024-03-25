

def Gold_fish(input_path, output_path):
    f = open(input_path, "r")

    N = int(f.readline()) #общее кол-во волшебных слов
    magic_words = []
    for i in range(0, N):
        magic_words.append(f.readline().strip())
    F = int(f.readline()) # количество букв, на которые могут начинаться искомые волшебные слова
    blocks_start = dict()
    for i in range(0, F):
        l = f.readline().strip()
        letter = l.strip().split(" ")[0]
        count = int(l.strip().split(" ")[1])
        blocks_start[letter] = count

    L = int(f.readline()) # количество букв, на которые могут заканчиваться искомые волшебные слова
    blocks_finish = dict()
    for i in range(0, L):
        l = f.readline().strip()
        letter = l.strip().split(" ")[0]
        count = int(l.strip().split(" ")[1])
        blocks_finish[letter] = count

    f.close()
    used_words_count = 0
    def s(a):
        cost = 0
        if (a[0] in blocks_start.keys()) and (a[-1] in blocks_finish.keys()):
            cost = blocks_start[a[0]] + blocks_finish[a[-1]]
        return cost
    #magic_words.sort(key=s)
    #magic_words.reverse()
    # for word in magic_words:
    #     if (word[0] in blocks_start.keys()) and (word[-1] in blocks_finish.keys()):
    #         if blocks_start[word[0]] != 0:
    #             if blocks_finish[word[-1]] != 0:
    #                 blocks_start[word[0]] = blocks_start[word[0]] - 1
    #                 blocks_finish[word[-1]] = blocks_finish[word[-1]] - 1
    #                 used_words_count += 1

    def get_min_letter_start():
        a = float("inf")
        let = ""
        for e in blocks_start.items():
            if a > e[1]:
                if e[0] in [t[0] for t in magic_words if t != ""]:
                    a = e[1]
                    let = e[0]
        return [let,a]
    def get_min_letter_finish():
        a = float("inf")
        let = ""
        for e in blocks_finish.items():
            if a > e[1]:
                if e[0] in [t[-1] for t in magic_words if t != ""]:
                    a = e[1]
                    let = e[0]
        return [let, a]

    def get_min_let():
        start_let = get_min_letter_start()
        finish_let = get_min_letter_finish()
        if start_let[1] < finish_let[1]:
            return ["start", start_let[0]]
        return ["finish", finish_let[0]]


    def get_max_letter_start():
        a = 0
        let = ""
        for e in blocks_start.items():
            if a < e[1]:
                if e[0] in [t[0] for t in magic_words if t != ""]:
                    a = e[1]
                    let = e[0]
        return [let,a]
    def get_max_letter_finish():
        a = 0
        let = ""
        for e in blocks_finish.items():
            if a < e[1]:
                if e[0] in [t[-1] for t in magic_words if t != ""]:
                    a = e[1]
                    let = e[0]
        return [let, a]

    def get_max_let():
        start_let = get_max_letter_start()
        finish_let = get_max_letter_finish()
        if start_let[1] > finish_let[1]:
            return ["start", start_let[0]]
        return ["finish", finish_let[0]]

    old_count = -1
    while used_words_count != old_count:
        type, let = get_min_let()
        old_count = used_words_count
        first_sort = []
        for i in range(0, len(magic_words)):
            if (magic_words[i] != "") and (magic_words[i][0] in [e[0] for e in blocks_start.items()]) and (magic_words[i][-1] in [e[0] for e in blocks_finish.items()]):
                if type == 'start':
                    if magic_words[i][0] == let:
                        #used_words_count += 1
                        #blocks_start[let] = blocks_start[let] - 1
                        #blocks_finish[magic_words[i][-1]] =  blocks_finish[magic_words[i][-1]] - 1
                        #if blocks_start[let] == 0:
                        #    del blocks_start[let]
                        #if blocks_finish[magic_words[i][-1]] == 0:
                        #    del blocks_finish[magic_words[i][-1]]
                        #magic_words[i] = ""
                        first_sort.append(magic_words[i])
                if type == 'finish':
                    if magic_words[i][-1] == let:
                        #used_words_count += 1
                        #blocks_finish[let] = blocks_finish[let] - 1
                        #blocks_start[magic_words[i][0]] = blocks_start[magic_words[i][0]] - 1
                        #if blocks_finish[let] == 0:
                        #    del blocks_finish[let]
                        #if blocks_start[magic_words[i][0]] == 0:
                        #    del blocks_start[magic_words[i][0]]
                        #magic_words[i] = ""
                        first_sort.append(magic_words[i])
        for q in range(0, len(first_sort)):
            type_max, max_let = get_max_let()
            if type_max == 'start':
                if first_sort[q][0] == max_let:
                    used_words_count += 1
                    blocks_start[let] = blocks_start[let] - 1
                    blocks_finish[first_sort[q][-1]] =  blocks_finish[first_sort[q][-1]] - 1
                    if blocks_start[let] == 0:
                       del blocks_start[let]
                    if blocks_finish[first_sort[q][-1]] == 0:
                       del blocks_finish[first_sort[q][-1]]
                    magic_words[q] = ""
            if type_max == 'finish':
                if first_sort[q][-1] == max_let:
                    used_words_count += 1
                    blocks_finish[let] = blocks_finish[let] - 1
                    blocks_start[first_sort[q][0]] = blocks_start[first_sort[q][0]] - 1
                    if blocks_finish[let] == 0:
                       del blocks_finish[let]
                    if blocks_start[first_sort[q][0]] == 0:
                       del blocks_start[first_sort[q][0]]
                    magic_words[q] = ""



    f = open(output_path, "w")
    f.write(str(used_words_count))
    f.close()
    return used_words_count

autocheck = False

if autocheck:
    for w in range(1, 14):
        q = str(w)
        if len(q) == 1:
            q = "0"+q
        print(q)
        out = Gold_fish("C:/Users/User/Downloads/Золотая рыбка/input_s1_"+q+".txt", "output.txt")
        f = open("C:/Users/User/Downloads/Золотая рыбка/output_s1_"+q+".txt")
        u = f.readline().strip()
        if out != int(u):
            print("ERROR")

else:
    print(Gold_fish("C:/Users/User/Downloads/Золотая рыбка/input_s1_03.txt", "output.txt"))




