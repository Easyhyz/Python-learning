# 罗马数字包含I、V、X、L、C、D、M，分别表示数值1、5、10、50、100、500、1000
# I可以放在V(5)和X(10)的左边，表示4、9
# X可以放在L(50)和C(100)的左边，表示40和90
# C可以放在D(500)和M(1000)的左边，表示400和900
# 函数 将输入的罗马字符转换为数字的形式
R2N = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # 初始化字典

# 转换
def roma2num(s):
    r = 0 # 初始化数字
    n = len(s)
    for i , ch in enumerate(s): # 同时获取索引和元素
        v = R2N[ch] # 取值
        if i < n-1 and v < R2N[s[i+1]]: # 判断是否是最后一个元素，比较值大小
            r -= v
        else:
            r += v

    return r;

# 判断输入是否正确
def checkroma(s):
    in_roma = 1
    for each in s:
        if each not in R2N:
            in_roma = 0
            break

    return in_roma

# 主程序
s = input('请输入一个罗马字符:(输入exit退出)')
while s != 'exit':
    if checkroma(s) == 0:
        s = input("请输入正确的罗马字符：")

    v = roma2num(s)
    print(f"转换后的结果是:{v}")
    print()
    s = input("请输入一个罗马字符:(输入exit退出)")

print("已退出~")