inp = [int(i) for i in input().split()]
n_i = inp[0] # количество денежных единиц в исходной денежной системе
c_i = inp[1:n_i] # соотношения между денежными единицами в исходной денежной системе

inp = [int(i) for i in input().split()]
k_i = inp[0] # количество несчастливых чисел в стране с исходной денежной системой
A_i = inp[1:k_i+1] # сами несчастливые числа

inp = [int(i) for i in input().split()]
n_k = inp[0] # количество денежных единиц в конечной денежной системе
c_k = inp[1:n_k] # соотношения между денежными единицами в конечной денежной системе

inp = [int(i) for i in input().split()]
k_k = inp[0] # количество несчастливых чисел в стране с конечной денежной системой
A_k = inp[1:k_k+1] # сами несчастливые числа

cash_i = [int(i) for i in input().split()] # представлние денежной суммы в исходной денежной системе

# print(n_i, c_i)
# print(k_i, A_i)
# print(n_k, c_k)
# print(k_k, A_k)
# print(cash_i)

def delete_bad_numbers(bad_numbers, money):
    out = money
    for n in bad_numbers:
        if out >= n:
            out = out-1
    return out

def add_bad_numbers(bad_numbers, money):
    out = money
    for n in bad_numbers:
        if out >= n:
            out = out+1
    return out


def cash_decompiler(multiplers, money, bad_numbers):
    low_money_out = 0
    multipler = 1
    for i in range(len(money)-1, -1, -1):
        low_money_out += delete_bad_numbers(bad_numbers, money[i])*multipler
        if i != 0:
            multipler = multipler * multiplers[i-1]
    return low_money_out

low_money_i = cash_decompiler(c_i, cash_i, A_i)

def cash_compiler(multiplers, low_money, bad_numbers):
    def get_current_multipler(multiplers, pos):
        mult = 1
        for p in range(pos, len(multiplers)):
            mult = mult*multiplers[pos]
        return mult

    out_slots = []
    for i in range(0, len(multiplers)+1):
        if i != len(multiplers)+1:
            app = low_money // get_current_multipler(multiplers, i)
            low_money = low_money - app * get_current_multipler(multiplers, i)
        else:
            app = low_money
        out_slots.append(app)

    for i in range(0, len(out_slots)):
        out_slots[i] = add_bad_numbers(bad_numbers, out_slots[i])
    return out_slots

rez = cash_compiler(c_k, low_money_i, A_k)
print(str(rez)[1:-1].replace(",", " "))

