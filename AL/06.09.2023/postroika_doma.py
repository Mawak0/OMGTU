f = open("input.txt", "r")
input_data = [int(i) for i in f.readlines()[0].split()]
f.close()
x, y, l, c1, c2, c3, c4, c5, c6 = input_data
xq = x
yq = y

# случаи (из стены с ремонтом макс без перестроя) (из стены с ремонтом макс и перестрой) (перестрой макс) (только вывоз старой)

# стоимость (из стены с ремонтом макс без перестроя)
def max_old_wall_cost(x, y, xq, yq):
    wall_trash = 0
    if x < y:
        x, y = y, x
        xq, yq = yq, xq
    x -= l
    if x < 0:
        wall_trash = abs(x)
        x = 0
    return c1*(l-wall_trash) + wall_trash*c2 + wall_trash*c6 + (xq+yq+y+x)*c5 + (xq+yq+y+x)*c4

# cost (из стены с ремонтом макс и перестрой)
def max_old_wall_and_rebuild(x, y, xq, yq):
    wall_trash = 0
    if x < y:
        x, y = y, x
        xq, yq = yq, xq
    x -= l
    wall_trash_to_repair = l
    if x < 0:
        wall_trash = abs(x)
        wall_trash_to_repair -= abs(x)
        x = 0
    if (xq + yq + y + x) < wall_trash:
        wall_trash_to_use = (xq + yq + y + x)
        wall_trash = wall_trash - (xq + yq + y + x)
        new_need_wall = 0
    else:
        wall_trash_to_use = wall_trash
        wall_trash = 0
        new_need_wall = (xq + yq + y + x) - wall_trash_to_use
    #print(new_need_wall, wall_trash, wall_trash_to_use, wall_trash_to_repair, wall_trash+wall_trash_to_use+wall_trash_to_repair)
    return c1 * (wall_trash_to_repair) + wall_trash * c2 + wall_trash * c6 + new_need_wall * c5 + new_need_wall * c4 + wall_trash_to_use*c2 + wall_trash_to_use*c3

# cost (перестрой)
def max_rebuild(x, y, xq, yq):
    wall_trash = l
    if (xq + yq + y + x) < wall_trash:
        wall_trash_to_use = (xq + yq + y + x)
        wall_trash = wall_trash - (xq + yq + y + x)
        new_need_wall = 0
    else:
        wall_trash_to_use = wall_trash
        wall_trash = 0
        new_need_wall = (xq + yq + y + x) - wall_trash_to_use
    return wall_trash * c2 + wall_trash * c6 + new_need_wall * c5 + new_need_wall * c4 + wall_trash_to_use * c2 + wall_trash_to_use * c3

# cost (только вывоз)
def max_util(x, y, xq, yq):
    wall_trash = l
    return wall_trash * c2 + wall_trash * c6 + (xq+yq+y+x) * c5 + (xq+yq+y+x) * c4

costs = [max_old_wall_cost(x, y, xq, yq), max_old_wall_and_rebuild(x, y, xq, yq), max_rebuild(x, y, xq, yq), max_util(x, y, xq, yq)]
#print(min(costs))
f = open("output.txt", "w")
f.write(str(min(costs)))
f.close()