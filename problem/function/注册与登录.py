import hashlib
# 4个函数，获取用户指令(get_ins())、注册(register())、登录(login())、MD5加密(encrypt())
# 使用字典作为数据库
# 注册时需要验证用户名是否存在
# 登录时需要验证用户名和密码是否匹配
# 密码保存需要使用MD5加密

# 函数声明

# 功能：获取用户指令
# 返回：字符串、用户指令(1/2/3)
def get_ins():
    print("================")
    print("1. 注册")
    print("2. 登录")
    print("3. 退出")

    ins = input("请输入指令：")
    while not(ins == '1' or ins == '2' or ins=='3'):
        print("指令错误, 请输入正确指令")
    print("================")

    return ins

# 功能：模拟论坛注册
def register():
    name = input("请输入用户名: ")
    while fishc_db.get(name): # 检测用户名是否存在
        print("该用户名已存在。。。")
        name = input("请重新输入用户名: ")

    passwd = input("请输入密码：") # 可以添加重复验证
#   _passwd = input("请再输入一次：")
#   if _passwd != passwd:
#       print("两次密码不一致")
    passwd = encrypt(passed) # 加密

    fishc_db[name] = passwd
    print("恭喜, 注册成功~")

# 功能：模拟论坛登录
def login():
    name = input("请输入用户名：")
    while not fishc_db.get(name):
        print("该用户不存在")
        name = input("请重新输入用户名：")

    passwd = input("请输入用户名：")
    while fishc_db.get(name) != encrypt(passwd):
        print("密码错误！")
        passwd = input("请重新输入用户名：")

    print("恭喜, 登录成功~")

# 功能：md5加密
# 返回：加密后的密文
def encrypt(plaintext): # 输入原码
    bstr = bytes(plaintext, 'utf-8')
    ciphertext = hashlib.md5(bstr).hexdigest() # 加密
    return ciphertext # 返回md5密文

# 论坛原始数据库
fishc_db = {}

# 主程序
print("欢迎来到鱼C论坛~")

ins = get_ins()

while ins != '3':
    if ins == '1':
        register()
    if ins == '2':
        login()

    ins = get_ins()