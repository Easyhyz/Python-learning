n = int(input()) # 学生人数

aver = 0
count = 0

if n == 0:
    print("average = 0")
    print("count = 0")

else:
    scores = list(map(int, input().split()))

    for score in scores:
        aver += score
        if score >= 60:
            count += 1

    print(f"average = {aver/len(scores):.1f}")
    print(f"count = {count}")