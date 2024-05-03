
class state:
    variants = []
    way = []


matrix  = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0]
]




def find_variants(v, used):
    vars = []
    for i in range(0, len(matrix)):
        if matrix[v-1][i] != 0:
            if i+1 not in used:
                vars.append(i+1)
    return vars

s = state()
s.variants = find_variants(1, [])
s.way = [1]
states = [s]

def work(s):
    if len(s.variants) == 0:
        return
    for v in s.variants:
        q = state()
        q.way = s.way[:]
        q.way.append(v)
        q.variants = find_variants(v, q.way)
        states.append(q)
    s.variants = []


work(s)
oldlen = -1
while oldlen != len(states):
    oldlen = len(states)
    for s in states:
        work(s)
cycles = []
roads = []
for s in states:
    if len(s.way) == len(matrix):
        if matrix[s.way[-1]-1][s.way[0]-1] != 0:
            s.way.append(s.way[0])
            cycles.append(s.way)
        else:
            roads.append(s.way)

print("Гамильтоновы циклы:")
for i in cycles:
    print(i)
print("-------------")
print("Гамильтоновы пути:")
for i in roads:
    print(i)
