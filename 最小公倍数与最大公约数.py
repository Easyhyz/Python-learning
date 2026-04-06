# 辗转相除法
M, N = map(int, input().split())
m, n = M, N
gcd_result = 0

if m > n:
    while m % n: # 辗转相除法
        gcd = m % n
        m, n = n, gcd
    else:
        gcd_result = n
else:
    m, n = n, m
    while m % n:
        gcd = m % n
        m, n = n, gcd
    else:
        gcd_result = n

lcm_result = (M*N) // gcd_result # 最小公倍数

print(gcd_result, lcm_result)