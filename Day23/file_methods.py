# with open("info.txt", "w") as fp:
#     fp.write("Hello World\nWelcome to broadway")

with open("info.txt", "r") as fp:
    data = fp.read() # Normal read
    print(data)

    fp.seek(0)  # seek() method changes the cursor position to the provided index
    data = fp.read(7)
    print(data)

    fp.seek(13)
    data = fp.readline()
    print(data)

    fp.seek(0)
    data = fp.readlines()
    print(data)

    print(fp.tell())

data = ["Python is a high level language\n", "Python is an interpreted language"]
with open("info.txt", "w") as fp:
    fp.writelines(data)
