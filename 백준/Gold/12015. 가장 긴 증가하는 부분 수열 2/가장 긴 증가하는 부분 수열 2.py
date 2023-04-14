import sys

def bisearch(left, right, target):
    mid = (left + right)//2
    if X[mid] < target:
        right -= 1
    elif X[mid] > target:
        left += 1
    if X[mid] == target:
        return mid
    


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
X = [A[0]]
for i in range(1, N):
    l = 1
    r = len(X)
    if X[-1] < A[i]:
        X.append(A[i])
    elif X[0] >= A[i]:
        X[0] = A[i]
    else:
        while l < r:
            mid = (l+r)//2
            if X[mid] < A[i]:
                l = mid + 1
            else:
                r = mid
        if X[l] > A[i] > X[l-1]:
            X[l] = A[i]
print(len(X))
