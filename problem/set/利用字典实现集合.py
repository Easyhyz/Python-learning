import random

# 随机1-100的数字
x = [random.randint(1, 100) for i in range(100)] # 循环100次生成100个数字
y = [random.randint(50, 100) for i in range(100)]

inter = dict.fromkeys([z for z in x if z in y]) # 求交集， 用fromkeys()去重
print(list(inter.keys()))