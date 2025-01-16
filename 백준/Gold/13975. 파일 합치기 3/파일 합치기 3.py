import sys
import heapq
input = sys.stdin.readline

T = int(input())
for t in range(T):
    K = int(input())
    C = list(map(int, input().split()))
    heapq.heapify(C) 
    # 파일 크기값들을 최소 힙으로 변환
    cost = 0
    while C: 
        # 파일들 중 작은 것들부터 합침
        q = heapq.heappop(C)
        if C:
            p = heapq.heappop(C)
            pq = p+q
            cost += pq
            # 합치는 과정에 두 파일의 합만큼 소모된 비용 누적
            heapq.heappush(C, pq) 
            # 합쳐진 새로운 파일을 힙에 추가
    print(cost)