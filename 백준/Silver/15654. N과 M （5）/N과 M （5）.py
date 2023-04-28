def sequence(subseq: list):
    global N
    if len(subseq) == M:
        print(*subseq)
        return
    for i in range(N):
        if seq[i] not in subseq:
            sequence(subseq+[seq[i]])

N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
sequence([])

