import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def union_parent(p):
    if parent[p] != p:
        parent[p] = union_parent(parent[p])
    return parent[p]


for test_case in range(1, 1 + T):
    N = int(input())

    x_point = list(map(int, input().split()))
    y_point = list(map(int, input().split()))
    E = float(input())

    lines = []

    # 간선 정보 저장
    for i in range(N):
        for j in range(i + 1, N):
            l2 = (x_point[i] - x_point[j]) ** 2 + (y_point[i] - y_point[j]) ** 2
            lines.append((i, j, l2))

    lines.sort(key=lambda x: x[2])
    parent = [i for i in range(N)]
    line_num = 0
    cost = 0

    while lines:
        node1, node2, L2 = lines.pop(0)
        if parent[node1] != parent[node2]:
            a = union_parent(node1)
            b = union_parent(node2)
            parent[b] = parent[a]
            cost += L2
            line_num += 1

        if line_num == N - 1:
            break

    print('parent : ', parent)
    answer = cost * E
    print(f'#{test_case} {answer}')
