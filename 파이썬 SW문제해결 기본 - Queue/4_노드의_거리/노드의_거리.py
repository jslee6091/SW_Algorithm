import sys
sys.stdin = open("노드의_거리_inputs.txt", 'r')

T = int(input())


def bfs(node, purpose):
    count = 1
    visit = [node]
    is_visit = [0 for _ in range(V + 1)]
    is_visit[node] = 1

    while len(visit) > 0:
        check2 = []
        while len(visit) > 0:
            check = visit.pop()
            for j in line[check]:
                if is_visit[j] == 1:
                    continue
                if j == purpose:
                    return count
                check2.append(j)
                is_visit[j] = 1

        count += 1
        visit = check2

    return 0


for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    line = [[] for _ in range(V+1)]
    for i in range(E):
        node1, node2 = map(int, input().split())
        line[node1].append(node2)
        line[node2].append(node1)

    start, end = map(int, input().split())

    result = bfs(start, end)

    print(f'#{test_case} {result}')
