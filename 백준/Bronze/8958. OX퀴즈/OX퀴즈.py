t = int(input())
for tc in range(t):
    bonus = 1
    score = 0
    for w in input():
        if w == "O":
            score += bonus
            bonus += 1
        else:
            bonus = 1
    print(score)
