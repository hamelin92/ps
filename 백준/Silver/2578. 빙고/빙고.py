board = []
ans = []
for _ in range(5):
	board += list(map(int, input().split()))
for _ in range(5):
	ans += list(map(int, input().split()))

bingo_cnt = [0]*12

for num in range(25):
	idx = divmod(board.index(ans[num]), 5)
	bingo_cnt[idx[0]] += 1
	bingo_cnt[5+idx[1]] += 1
	if idx[0] == idx[1]:
		bingo_cnt[10] += 1
	if 4 - idx[0] == idx[1]:
		bingo_cnt[11] += 1
	if bingo_cnt.count(5) >= 3:
		print(num+1)
		break
