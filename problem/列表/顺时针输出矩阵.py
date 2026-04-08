m, n = map(int, input().split())

matrix = [[0]*n for _ in range(m)]
result = []

num = 1
for row in range(m):
    for col in range(n):
        matrix[row][col] = num
        num += 1
print(matrix, end='\n')

rows = m
cols = n
top = 0
bottom = m-1
left = 0
right = n-1

while left <= right and top <= bottom:
    # 从左到右
    for col in range(left, right+1):
        result.append(matrix[top][col])
    # 从上到下
    for row in range(top+1, bottom+1): # top行执行过，top下移
        result.append(matrix[row][right])
    # 从右到左
    for col in range(right-1, left, -1): # right列执行过，right左移，执行不到left本身
        result.append(matrix[bottom][col])
    # 从下到上
    for row in range(bottom, top, -1):
        result.append(matrix[row][left])

    top += 1
    bottom -= 1
    left += 1
    right -= 1

print(result)