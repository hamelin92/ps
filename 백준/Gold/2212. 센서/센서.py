import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = int(input()), int(input())
sensor = list(map(int, input().split()))

sensor.sort() # 센서들을 좌표 순서대로 정렬

diff = [sensor[i+1] - sensor[i] for i in range(N-1)]
# 센서들간의 좌표 간격

diff.sort() # 센서 좌표간의 간격을 다시 크기 순으로 정렬
# 간격이 가장 긴 경우는 하나의 집중국으로 묶이지 않을 수 있으면 좋다.
# 즉, K개의 집중국을 나누는 K-1개의 구간이 있다면 그 구간들은 센서 좌표의 간격이 가장 큰 것들을 K-1개만큼 고른 것.

print(sum(diff[:N-K]))