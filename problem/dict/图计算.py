n = int(input())

graph = {}

for each in range(n):
    line = input()
    vertex_dict = eval(line) # 识别转换成对应的形式(字典)
    graph.update(vertex_dict) # 更新到graph中

vertex_count = len(graph) # 统计顶点的个数

edge_count = 0
total = 0

for vertexs, edges in graph.items():
    edge_count += len(edges)
    total += sum(edges.values())

print(vertex_count, edge_count, total)