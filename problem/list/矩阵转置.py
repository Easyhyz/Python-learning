# 正常循环实现矩阵转置
m, n = map(int, input().split())

matrix = [[0] * n for _ in range(m)] # _ 不表示任何意思，仅代表循环m次
num = 1
for row in range(m): # 自增
    for col in range(n):
        matrix[row][col] = num
        num += 1

print("原矩阵：")
for row in range(m):
    for col in range(n):
        print(matrix[row][col], end='   ')
    print()
print()

transpoted = []
for i in range(n):
    transpoted.append([row[i] for row in matrix])
# transpoted = [[row[i] for row in matrix] for i in range(n)]
# 先竖再横
"""
1 2 3
4 5 6
7 8 9
"""
"""
1 4 7
2 5 8
3 6 9
"""

print("转置矩阵：")
for row in range(n):
    for col in range(m):
        print(transpoted[row][col], end='   ')
    print()
