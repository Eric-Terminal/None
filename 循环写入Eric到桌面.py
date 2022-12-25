path=r"/Users/lilin/Desktop/123.txt"
A = "Eric"
while True:
    with open(path, 'w') as f:
        f.write(A)
        f.write("\n")
