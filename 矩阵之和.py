m, n = map(int, input().split())

for i in range(m):
    row = list(map(int, input().split())) # 矩阵切分求和
    print(sum(row))