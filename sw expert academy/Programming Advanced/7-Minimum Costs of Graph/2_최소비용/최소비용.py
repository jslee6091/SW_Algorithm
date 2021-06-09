import sys
from collections import deque
sys.stdin = open("최소비용_inputs.txt", 'r')

T = int(input())

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Dijkstra Algorithm 활용한 최소비용 구하기
for test_case in range(1, 1 + T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')

    # 도착까지 드는 비용 표시 - 모두 무한대
    distance = [[INF for _ in range(N)] for _ in range(N)]
    # 처음 부분은 0으로 초기화
    distance[0][0] = 0
    queue = deque()
    # 0,0 부터 시작
    queue.append((0, 0))

    # 큐가 비어있을 때까지 반복
    while queue:
        y, x = queue.popleft()

        # 이동할 방향 선택 - 상,하,좌,우
        for dy, dx in move:
            my, mx = dy + y, dx + x
            # graph 범위를 벗어나지 않으면 실행
            if 0 <= my < N and 0 <= mx < N:
                # 기본 이동비용 1
                temp = 1
                # 현재 위치와 다음 위치의 높이차만큼 추가 - 다음위치가 더 높으면 추가
                if graph[my][mx] > graph[y][x]:
                    temp += graph[my][mx] - graph[y][x]

                # 다음 위치의 거리가 현재 위치의 거리 + temp 보다 크다면 값을 바꿈
                # 다음 위치가 처음 방문하는 경우이거나 이미 방문했는데 현재위치에서 이동하면 거리가 더 짧아지는 경우
                if distance[my][mx] > distance[y][x] + temp:
                    distance[my][mx] = distance[y][x] + temp
                    queue.append((my, mx))

    answer = distance[N - 1][N -1]
    print(f'#{test_case} {answer}')
