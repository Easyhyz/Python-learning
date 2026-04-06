m, n = map(int, input().split())
found = 0

for num in range(m, n+1):
    y = []
    total = 0
    for i in range(1, int(num**0.5)+1): # 运行超时
        if num%i == 0:
           y.append(i)
           total += i

           _i = num // i # 通过一次性存储除数与商解决
           if _i != i and _i != num:
               y.append(_i)
               total += _i

    y.sort()
           
    if num == total:
        y_str = " + ".join(map(str, y))
        print(f"{num} = {y_str}") # 格式化输出6 = 1 + 2 +3
        found = 1
if found == 0:
    print("None")