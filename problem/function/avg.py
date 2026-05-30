"""
每次传入一个参数，返回所有参数的平均值
重置数据
"""

count = 0
nsum = 0
def make_avg():
    def _avg(a):
        global count, nsum
        count += 1
        nsum += a
        return nsum / count
    
    return _avg
        
a = int(input("请输入数字：(输入0退出, 输入-1重置)"))
while (a != 0):
    if (a == -1):
        count, nsum = 0, 0
        print("重置成功！")
        a = int(input("请输入数字：(输入0退出, 输入-1重置)"))
    else:
        avg = make_avg()
        print(avg(a))
        a = int(input("请输入数字：(输入0退出, 输入-1重置)"))
    

print("退出成功")