import random
def random_password():
    upper_words_list = []  # 大写
    lower_words_list = []  # 小写
    num_list = []  # 数字
    for i in range(65, 90):
        upper_words_list.append(chr(i))
    for i in range(97, 122):
        lower_words_list.append(chr(i))
    for i in range(0, 10):
        num_list.append(i)
    total_list = upper_words_list + lower_words_list + num_list
    while True:  # 可任意设置密码个数
        password = random.sample(total_list, 8)  # 8位随机
        password_str = ''.join(str(e) for e in password)  # list 转化为str
        print(password_str)
if __name__ == '__main__':
    random_password()