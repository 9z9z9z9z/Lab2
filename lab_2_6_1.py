path = "article_rus.txt"
base = "йцукенгшщзхъэюждбьлотирпмсавчяыфё"
count = 0
data = {}

for i in range(33):
    data[base[i]] = 0

with open(path, 'r', encoding="utf-8") as file:
    database = file.read()
    for i in database:
        if i in base:
            count += 1
            data[i] += 1

for i in range(33):
    print(str(base[i]) + " : " + str(round(data[base[i]] / count, 3)))

