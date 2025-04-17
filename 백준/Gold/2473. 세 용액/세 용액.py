import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input()) # 용액의 수 3~5000
chars = list(map(int, input().split())) # N개의 특성값 (+-1~1,000,000,000)
chars.sort()
results = [1000000001, 1000000001, 1000000001]
v = 3000000003
for k in range(N-1):
    i = k+1
    j = N-1
    while i < j:
        ph = chars[i] + chars[j] + chars[k]
        if abs(ph) < v:
            results = [chars[k], chars[i], chars[j]]
            v = abs(ph)
        if ph < 0:
            i += 1
        elif ph >0:
            j -= 1
        else:
            break

print(*results)