N = int(input())
ans = 0
while N > 4:
    N //=5
    ans += N
print(ans)
