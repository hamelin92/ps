N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
cnt = [[0]*7 for _ in range(2)]
rooms = [[0]*7 for _ in range(2)]
for student in students:
    cnt[student[0]][student[1]] += 1
    if rooms[student[0]][student[1]] == 0:
        rooms[student[0]][student[1]] = 1
    elif cnt[student[0]][student[1]] > K:
        cnt[student[0]][student[1]] -= K
        rooms[student[0]][student[1]] +=1

print(sum(rooms[0]) + sum(rooms[1]))