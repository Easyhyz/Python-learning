second_team = {6, 7, 8, 9, 10} # 第二小队集合

vote_str = input()

vote_set = set(map(int, vote_str.split(','))) # 格式化

not_voted = second_team - vote_set # 集合运算

result = ' '.join(map(str, sorted(not_voted)))
print(result)