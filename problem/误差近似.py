error = float(input()) # 误差是浮点数
e = 1
f = 1
n = 1 # 阶乘项要单独判断

while True:
    f *= n
    e += 1/f
    if 1/f < error:
        print(f"{e:.6f}")
        break
    
    n = n+1