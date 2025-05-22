import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
h = list(map(int, input().split()))
sh = sum(h)
num = sh//3

if sh%3 == 0:
    boundary = sum(map(lambda x: x//2, h))
    if boundary >= num:
        print("YES")
    else:
        print("NO")
else:
    print("NO")