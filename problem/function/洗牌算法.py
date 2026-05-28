"""
封装一个fy_shuffle函数
参数1：可迭代对象类型，存储原始的数据
参数2：整数类型，指定洗牌的次数
返回值：列表类型，存储打乱后的数据
"""

import random

# 功能：打乱序列
# 参数：data, times
def fy_shuffle(data, times):
    # 初始化结果
    result = list(data)
    for i in range(times):
        target = list(result) # 创建当前结果的副本 类似copy？
        result = []
        while target:
            r = random.randint(0, len(target)-1)
            result.append(target.pop(r))
            
        print(f"第{i+1}次打乱后的结果：{''.join(result)}")
        
    return "".join(result)

data = input("请输入要打乱的序列:")
times = int(input("请输入要打乱的次数:"))

print(f"最终结果是: {fy_shuffle(data, times)}")