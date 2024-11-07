N = int(input())
numbers = list(map(int, input().split()))
ans = 0
i = j = l =0
check = [0]*100001
while j < N:
    if not check[numbers[j]]:
        check[numbers[j]] = 1
        l += 1
        j += 1
        ans += l
    else:
        check[numbers[i]] = 0
        i += 1
        l -= 1
print(ans)