import sys, math


input = lambda: sys.stdin.readline().rstrip()
dp = [0]*1000001
dp[1] = 1
dp[3] = 1
squares = [i**2 for i in range(1001)]
for i in range(1000001):
	if dp[i] == 0:
		for n in range(1, math.floor((1000000-i)**(1/2))+1):
			dp[i+squares[n]] = 1
T = int(input())
for t in range(T):
	N = int(input())
	if dp[N] == 1:
		print("koosaga")
	else:
		print("cubelover")