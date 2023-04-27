def sequence(last: int, depth: int):
    global N
    if depth == M:
        print(*seq)
        return
    for i in range(last, N+1):
        seq[depth] = i
        sequence(i, depth + 1)

N, M = map(int, input().split())
seq = [0] * M
sequence(1, 0)

