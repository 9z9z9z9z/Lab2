import os

tmp = input("Input 2 numbers: left/right\n")

tmp_num = tmp.split("/")
path = "example\\"
left = int(tmp_num[0])
right = int(tmp_num[1])

count = 0

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    if left * 1024 <= os.path.getsize(f) and os.path.getsize(f) <= right * 1024:
        count += 1

print("Number of files\t", count)

