list_name = []
sorted_list_2 = []

with open("players.csv", 'r', encoding="utf-8") as players_base:
    flag = True
    for i in players_base:
        str_tm = i.replace('\n', "")
        str_tm = str_tm.split(';')
        if not flag:
            name = (str_tm[0], int(str_tm[1]), int(str_tm[2]))
            list_name.append(name)
        flag = False


sorted_list = (sorted(list_name, key=lambda player: (player[1], player[2])))

players_save = open("results.csv", 'w', encoding="utf-8")

for i in range(len(sorted_list) - 1, 0, -1):
    save = str(sorted_list[i][0]) + ";" + str(sorted_list[i][1]) + ";" + str(sorted_list[i][2])
    players_save.write(str(save) + '\n')
