# 将数字转换为罗马字符的形式
# 构建N2R，加入CM、CD、XL、IX、IV

# 使用列表嵌套元组，天然有序，使用字典也可，3.7以下版本字典无序
N2R = [(1000, 'M'),
       (900, 'CM'),
       (500, 'D'),
       (400, 'CD'),
       (100, 'C'),
       (90, 'XC'),
       (50, 'L'),
       (40, 'XL'),
       (10, 'X'),
       (9, 'IX'),
       (5, 'V'),
       (4, 'IV'),
       (1, 'I')]

# 数字转换成罗马数字
def num2roma(num):
    result = []
    for v, s in N2R:
        while num >= v:
            num -= v
            result.append(s)
        if num == 0:
            break

    return "".join(result) # 列表转换字符串

# 判断输入是否属于数字的方法
# 1.try-except，通过float()返回True or False
# 2.字符串的isdigit()、isnumeric()、isdecimal()
# 3.使用正则表达式
# 4.使用isinstance(x, int)

# 主程序
# 添加循环
num = input("请输入一个整数:(输入exit退出)")
while num != 'exit':
    result = num2roma(int(num))
    print(f"转换后的结果是:{result}")
    print()
    num = input("请输入一个整数:(输入exit退出)")
print("退出成功~")