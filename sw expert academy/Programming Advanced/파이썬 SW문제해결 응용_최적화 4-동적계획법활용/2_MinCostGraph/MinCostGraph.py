import sys
sys.stdin = open("MinCostGraph_inputs.txt", 'r')

T = int(input())

# 참고 : https://daep93.github.io/2020/05/14/SW-5263/
# 그래프에서 특정 노드 사이의 최단 경로를 구하는 문제
for test_case in range(1, T + 1):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                if adj[i][j] == 0:
                    adj[i][j] = float('inf')
    '''
    만약 k가 0이라면 sub for문을 다 돌았을 때, 0을 경유했을 때 더 짧은지 이미 비교가 된 상태이다. 
    만약 k가 1이라면 이전 결과와 1을 경유했을 때 결과를 비교하는 꼴이므로, 
    모든 vertex(k!=i,j)에 대해서 경유했을 때 결과적으로 어떤 vertex를 지났을 때 가장 짧은지를 알 수 있다.
    '''
    for k in range(N):
        for i in range(N):
            if i == k:
                continue
            for j in range(N):
                if k == i or k == j or i == j:
                    continue
                else:
                    adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])
    max_val = 0
    for row in adj:
        max_row = max(row)
        if max_row > max_val:
            max_val = max_row

    print(f'#{test_case} {max_val}')
