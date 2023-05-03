import sys

def tri_star(r, c, n):
    if n <= 3:
        board[r][c-1] = "*"
        board[r+1][c-2] = "*"
        board[r+1][c] = "*"
        board[r+2][c-3:c+2] = ["*"]*5
        return
    tri_star(r, c, n//2)
    tri_star(r+n//2, c-n//2, n//2)
    tri_star(r+n//2, c+n//2, n//2)

N = int(sys.stdin.readline())
board = [[" "]*(2*N-1) for _ in range(N)]
tri_star(0, N, N)
for i in range(N):
    sys.stdout.write(str(board[i]).replace("', '", "").strip("['").strip("']")+"\n")