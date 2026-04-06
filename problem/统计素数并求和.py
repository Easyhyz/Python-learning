m, n = map(int, input().split())

total = 0 # 用total避免sum函数冲突
count = 0

for i in range(m, n+1):
    is_su = 1
    if i <= 1: # 跳过不大于1的数
        continue
    for j in range(2, int(i/2) + 1): # 范围加一
        if i%j == 0:
            is_su = 0
            break
    if is_su: # 只有判断完素数后再xjia
        total += i
        count += 1

print(count, total)