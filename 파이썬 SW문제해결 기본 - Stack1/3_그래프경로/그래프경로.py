import sys

sys.stdin = open("그래프경로_inputs.txt", 'r')

T = int(input())


def dfs(node):
    location[node] = False
    for var in graph[node]:
        if location[var]:
            dfs(var)


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    location = [True] * (V+1)
    answer = 1

    for idx in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    start_node, end_node = map(int, input().split())
    dfs(start_node)

    if location[end_node]:
        answer = 0

    print(f'#{test_case} {answer}')
