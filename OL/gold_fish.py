

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
    magic_words.sort(key=s)
    magic_words.reverse()
    for word in magic_words:
        if (word[0] in blocks_start.keys()) and (word[-1] in blocks_finish.keys()):
            if blocks_start[word[0]] != 0:
                if blocks_finish[word[-1]] != 0:
                    blocks_start[word[0]] = blocks_start[word[0]] - 1
                    blocks_finish[word[-1]] = blocks_finish[word[-1]] - 1
                    used_words_count += 1

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
    print(Gold_fish("C:/Users/User/Downloads/Золотая рыбка/input_s1_01.txt", "output.txt"))





