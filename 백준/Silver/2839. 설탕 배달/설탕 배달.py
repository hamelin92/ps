N = int(input())
col = [0, 1, 2, 1, 2]
if N == 4 or N == 7:
	print(-1)
else:
	print(N//5+col[N%5])