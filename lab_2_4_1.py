import os
from random import randint

# Функция генерации файла
def generate(path):
    n = 100
    for i in range(n):
        size = randint(1, 100)
        with open(path + str(i + 1), "wb") as file:
            file.truncate(size * 1024)
            file.seek(size * 1024 - 1)
            file.write(b"\0")


path = "example\\"
os.mkdir("example")
generate(path)


