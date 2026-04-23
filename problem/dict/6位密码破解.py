import hashlib

# 生成0-999999的所有整数组成密码的哈希值
hash_list = {}
for each in range(1000000):

    str_each = bytes(str(each), 'utf-8')
    s = hashlib.md5(str_each).hexdigest()
    hash_list[s] = each

# 保存为映射类型
# 查表计算密码
passwd_hash = input("请输入哈希值（输入exit退出）")
while passwd_hash != 'exit':
    print(hash_list.get(passwd_hash))
    passwd_hash = input("请输入哈希值（输入exit退出）")
print("已退出")