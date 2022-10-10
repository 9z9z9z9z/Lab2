from random import randint


def generate(ip, n):
    for i in range(n):
        tmp_ip = []
        for i in range(4):
            part = randint(0, 255)
            tmp_ip.append(part)
        ip.append(tmp_ip)


IPs = []
n = 10000
path = "ip.log"

generate(IPs, n)

with open(path, "w") as file:
    for ip in range(n):
        for part in range(3):
            file.write(str(IPs[ip][part]))
            file.write(".")
        file.write(str(IPs[ip][3]))
        file.write("\n")

print("Ended")
