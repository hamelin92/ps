import sys

N = int(sys.stdin.readline())
nums = sorted(int(sys.stdin.readline()) for _ in range(N))
print(*nums, sep="\n")
