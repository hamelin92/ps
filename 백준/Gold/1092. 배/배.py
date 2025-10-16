import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
crane.sort(reverse=True)
box.sort(reverse=True)
cnt = 0
if box[0] > crane[0]:
	print(-1)
else:
	while box:
		for c in crane:
			if box and c < box[-1]:
				continue
			for b in box:
				if c >= b:
					box.remove(b)
					break
		cnt += 1
	print(cnt)