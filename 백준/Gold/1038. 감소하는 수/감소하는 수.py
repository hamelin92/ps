from itertools import combinations

N = int(input())

# n자리 감소하는 수는 9876543210 에서 서로 다른 숫자 n개를 선택하면 결정된다.
nums = [0]*11 # 리스트의 i번째 원소가 i자리 이하의 감소하는 수의 갯수를 나타내도록 한다.
nums[0] = 1

for i in range(1, 11):
    nums[i] = (nums[i-1]*(11-i))//i

if N > 1022:
    print(-1)
else:
    r = 0 # 자리수
    k = N+1 # 같은 자리 수 내에서의 순서
    for i in range(11):
        if k >= nums[i]:
            k = k-nums[i]
            r = i
        else:
            if k >= 0:
                r += 1
            break
    choice = list(combinations(range(9,-1,-1), r))[-k-1]
    ans = ""
    for i in range(r):
        ans += str(choice[i])
    print(ans)