N = int(input())
M = round(N*(-1+(5**(1/2)))/2)
result = []
for idx in range(3):
    seq1 = N
    seq2 = M-1+idx
    seqs = [seq1, seq2]
    seq = seq1 - seq2
    while seq >= 0:
        seqs.append(seq)
        seq1 = seq2
        seq2 = seq
        seq = seq1 - seq2
    result.append(seqs)
result.sort(key=len)
print(len(result[-1]))
print(*result[-1])