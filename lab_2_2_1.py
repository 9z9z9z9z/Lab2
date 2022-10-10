def input_IP():
    flag = True
    while flag:
        string = input("Input mask\n")
        string = string.split(".")
        mask = list()

        for part in string:
            mask.append(int(part))
        k = 0
        for part in mask:
            if part < 0 or part > 255:
                k += 1
        if k == 0:
            flag = False
    return mask


base = "ip.log"
save = "ip_solve.log"

mask = input_IP()

with open(base, "r") as file:
    string = file.read()
    string = string.split("\n")
    for i in range(10000):
        string[i] = string[i].split(".")

base = list()  # Список IP адресов
net_ip = list()  # Список интернет адресов

for ip_ in string:
    tmp_ip = list()
    for part in ip_:
        tmp_ip.append(int(part))
    base.append(tmp_ip)

for index in range(10000):
    tmp_ip = list()
    for i in range(4):
        tmp_ip.append(base[index][i] & mask[i])
    net_ip.append(tmp_ip)

with open(save, "w") as file:
    for ip in range(10000):
        for part in range(3):
            file.write(str(net_ip[ip][part]))
            file.write(".")
        file.write(str(net_ip[ip][3]))
        file.write("\n")

print("end")
