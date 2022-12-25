import hashlib

# 待加密信息
str = input("MD5原文:")

# 创建md5对象
hl = hashlib.md5()
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())