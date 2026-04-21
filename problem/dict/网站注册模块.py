# 初始用户及密码
users = {"小甲鱼":"I_love_FishC", "不二如是":"FishC5201314"}
# 用户名不许重复
# 保存用户名及密码

name = input("请输入用户名: ")
while True:
    if users.get(name) != None:
        print("该用户名已被注册！")
        name = input("请重新输入用户名: ")
    else:
        break

passwd = input("请输入密码: ")
users[name] = passwd # 注册的新用户添加到users中

print("----------------")
print("目前已注册的用户有：")
for each in users:
    print(each)