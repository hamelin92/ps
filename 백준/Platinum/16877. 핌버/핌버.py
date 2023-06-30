import sys
input = sys.stdin.readline

n = int(input())
p_max = 3000001
F = [1, 1]
fib = 0
while F[-1] < p_max:
    F.append(F[fib]+F[fib+1])
    fib += 1
g = [0]*p_max
# g[i] : 상태 i에서 다음 상태로 진행될 떄 될 수 없는 가장 작은 0 이상의 정수
for i in range(1, p_max):
    check = [False]*33
    # check : g[i] 값이 될 수 있는 값들의 범위를 크기로 한 배열
    for j in range(1, 32):
        if F[j] > i:
            break
        check[g[i-F[j]]] = True
            # i 라는 상태에서 j라는 값을 뺄 수 있으므로 상태 i-j는 존재한다. 그러므로 g[i]의 값은 g[i-j]가 될 수 없다.
    for k in range(33):
        if not check[k]:
            g[i] = k
            break        
res = 0
for pi in map(int, input().split()):
    res ^= g[pi]
    # 각 i번째 돌의 개수에 대해 그런디 수 g[i]를 xor 연산
if res:
    print("koosaga")
else:
    print("cubelover")