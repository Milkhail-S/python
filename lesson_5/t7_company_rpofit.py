import json


f_name = 't7.txt'

total = {}
ap = 0
i = 0
with open(f_name, 'r', encoding='utf-8') as fi:
    for line in fi:
        lst = line.split()
        profit = int(lst[2]) - int(lst[3])
        net = profit if profit > 0 else int(lst[3])
        total.update({line[:line.index(' ')]: net})
        if profit > 0:
            ap += profit
            i += 1
    average_profit = ap / i
    total.update({'average_profit': round(average_profit, 2)})
    print(total)
with open('t7_data.json', 'w') as fi_j:
    json.dump(total, fi_j)
