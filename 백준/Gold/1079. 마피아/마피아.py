N = int(input())
guilty = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
me = int(input())
max_nights = 0

def possible_game(days:int, lived: set, guilty_now: list):
    global max_nights, me
    if N//2 == max_nights:
        return
    if days > max_nights:
        max_nights = days
    if len(lived)%2:
        targets = sorted(list(lived))
        punished = targets[0]
        for target in targets:
            if guilty_now[target] > guilty_now[punished]:
                punished = target
        if punished == me:
            return
        else:
            possible_game(days, lived-{punished}, guilty_now)
    else:
        targets = list(lived)
        for target in targets:
            if target != me:
                new_guilty = guilty_now[:]
                for j in range(N):
                    if j != target:
                        new_guilty[j] += R[target][j]
                possible_game(days+1, lived-{target}, new_guilty)

possible_game(0, set(range(N)), guilty)
print(max_nights)