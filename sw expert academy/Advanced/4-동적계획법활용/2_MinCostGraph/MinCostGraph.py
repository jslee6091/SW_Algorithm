import sys
sys.stdin = open("MinCostGraph_inputs.txt", 'r')

T = int(input())

# 참고 : https://daep93.github.io/2020/05/14/SW-5263/
# 모든 쌍 최단 경로 알고리즘 (All Pairs Shortest Path)
# Floyd-Warshall Algorithm
for test_case in range(1, T + 1):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                # 두 정점 사이의 경로가 없으면 무한대로 바꿈
                if adj[i][j] == 0:
                    adj[i][j] = float('inf')

    # Floyd-Warshall Algorithm 의 핵심
    for k in range(N):
        for i in range(N):
            if i == k:
                continue
            for j in range(N):
                if k == j or i == j:
                    continue
                else:
                    # i에서 k를 거쳐 j로 가는 경로의 값과 직접 가는 경로의 값 중 더 작은 것 선택
                    adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])

    # 최대값 구하기
    max_val = 0
    for row in adj:
        max_row = max(row)
        if max_row > max_val:
            max_val = max_row

    print(f'#{test_case} {max_val}')
