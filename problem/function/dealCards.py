"""
斗地主游戏由54张牌组成，两张Joker
游戏人数3人，一人地主另外两人农民
发牌规则：每人先发17张，留三张地主牌，随机抽一名地主
"""

import random

cards = ["♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
         "♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
         "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K",
         "♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
         "☀", "🌙"]

# 功能：打乱序列
# 参数：data, times
def fy_shuffle(data, times):
     # 初始化结果
    result = list(data)
    for i in range(times):
        target = list(result) # 创建当前结果的副本 类似copy？
        result = []
        while target:
            r = random.randint(0, len(target)-1)
            result.append(target.pop(r))
        
    return result
    
# 功能：发牌
# 参数：无
def dealCards():
    a = input("请输入第一位游戏玩家名称:")
    b = input("请输入第二位游戏玩家名称:")
    c = input("请输入第三位游戏玩家名称:")
    
    new_cards = fy_shuffle(cards, 3)
    r = {} # 创建手牌库
    r[a], r[b], r[c] = [], [], [] # 初始化手牌
    
    for i in range(17): # 发牌
        r[a].append(new_cards.pop())
        r[b].append(new_cards.pop())
        r[c].append(new_cards.pop())
    
    # 选地主
    d = random.sample((a, b, c), 1)[0]
    print(f"\n地主是{d}\n")
    r[d].extend((new_cards.pop(), new_cards.pop(), new_cards.pop()))
    
    # 输出
    print(f"{a}拿到的牌是{' '.join(r[a])}\n")
    print(f"{b}拿到的牌是{' '.join(r[b])}\n")
    print(f"{c}拿到的牌是{' '.join(r[c])}\n")
    
dealCards()