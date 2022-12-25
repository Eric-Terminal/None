while True:
    print("你要使用while还是for循环？")
    A = input("")
    if A == "while":
        # while循环
        Eric = 0
        while Eric < 3000:
            print("我爱你")
            Eric = Eric + 1
    if A == "for":
        # for循环
        for Eric in range(1, 3001):
            print("我爱你")