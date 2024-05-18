

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
    for l in blocks_start:
        l_available = blocks_start[l]
        l_demand = 0
        for w in magic_words:
            if w[0] == l:
                l_demand += 1
        used_words_count += min([l_demand, l_available])

    used_words_count_finish = 0

    for l in blocks_finish:
        l_available = blocks_finish[l]
        l_demand = 0
        for w in magic_words:
            if w[-1] == l:
                l_demand += 1
        used_words_count_finish += min([l_demand, l_available])

    if used_words_count != used_words_count_finish:
        #print(used_words_count, used_words_count_finish)
        used_words_count = min([used_words_count, used_words_count_finish])



    f = open(output_path, "w")
    f.write(str(used_words_count))
    f.close()
    return used_words_count


print(Gold_fish("C:/Users/user/Downloads/Золотая рыбка/input_s1_03.txt", "output.txt"))




