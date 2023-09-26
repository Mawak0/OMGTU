import numpy as np

def coster(val_milk1, val_paper1, val_milk2, val_paper2, cost1, cost2): #рассчитывает стоимость молока и упаковки отдельно
    left_side = np.array([[val_milk1, val_paper1], [val_milk2, val_paper2]])
    right_side = np.array([cost1, cost2])
    out = np.linalg.inv(left_side).dot(right_side)
    return out

f = open('input.txt', "r")
input_data = f.readlines()
f.close()
factories_count = int(input_data[0])
min_cost = [9999999, 9999999] #number, cost
for i in range(factories_count):
    data = input_data[i + 1].split()
    x1 = int(data[0])
    y1 = int(data[1])
    z1 = int(data[2])
    x2 = int(data[3])
    y2 = int(data[4])
    z2 = int(data[5])
    cost1 = float(data[6])
    cost2 = float(data[7])
    val_milk1 = x1 * y1 * z1
    val_paper1 = 2*(x1*y1+x1*z1+z1*y1)
    val_milk2 = x2 * y2 * z2
    val_paper2 = 2*(x2*y2+x2*z2+z2*y2)
    cost_milk, cost_paper = coster(val_milk1, val_paper1, val_milk2, val_paper2, cost1, cost2)
    cost_milk = round(cost_milk*1000, 2)
    cost_paper = round(cost_paper*1000, 2)
    if min_cost[1] > cost_milk:
        min_cost[1] = cost_milk
        min_cost[0] = i+1
    elif min_cost[1] == cost_milk:
        if min_cost[0] > i+1:
            min_cost[0] == i+1

#print(min_cost)
f = open('output.txt', 'w')
if len(str(min_cost[1])) < 4:
    min_cost[1] = str(min_cost[1])+"0"
f.write(f"{min_cost[0]} {min_cost[1]}")