"""
每次调用返回一个斐波那契数列
"""

def fib():
    fib1, fib2 = 0, 1
    def _fib():
        nonlocal fib1, fib2
        temp = fib1
        fib1, fib2 = fib2, fib1 + fib2
        return temp
    return _fib

f = fib()
times = int(input("请输入次数："))
for i in range(times):
    print(f())