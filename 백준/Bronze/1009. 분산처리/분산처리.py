T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    a %= 10
    b = (b-1)%4 + 1
    ans = 0
    if a == 1 or a == 5 or a == 6:
        ans = a
    else:
        ans = (a**b)%10
    if ans == 0:
        print(10)
    else:
        print(ans)