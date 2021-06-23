import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# Kruskal Algorithm - 모든 정점을 연결하는 최소 비용 신장 트리를 만들고 총 비용 구하기
# 노드의 루트를 찾는 함수
def union_parent(p):
    # 인덱스와 값이 다르면 자신이 루트가 아니므로 루트를 찾는다.
    if parent[p] != p:
        parent[p] = union_parent(parent[p])
    # 인덱스와 값이 같으면 자기 자신이 루트이다.
    return parent[p]


for test_case in range(1, 1 + T):
    N = int(input())

    # 정점의 x, y 좌표 입력 받기
    x_point = list(map(int, input().split()))
    y_point = list(map(int, input().split()))
    # 비용 계산할 때 곱하는 상수
    E = float(input())

    lines = []

    # 간선 정보 저장 - 각 노드들을 서로 연결하는 모든 경우에 대하여 거리 계산
    for i in range(N):
        for j in range(i + 1, N):
            l2 = (x_point[i] - x_point[j]) ** 2 + (y_point[i] - y_point[j]) ** 2
            lines.append((i, j, l2))

    # 오름차순 정렬
    lines.sort(key=lambda x: x[2])
    # 노드의 집합을 확인하기 위한 리스트
    parent = [i for i in range(N)]
    # 간선의 수와 전체 비용
    line_num = 0
    cost = 0

    # 간선의 수가 전체 노드를 연결할때까지 실행
    while line_num != N - 1:
        node1, node2, L2 = lines.pop(0)
        # node1과 node2의 루트 노드가 다르면 서로 연결 되지 않은 상태
        if parent[node1] != parent[node2]:
            # 각 노드의 루트 노드 구하기 - 이때 연결된 후 갱신이 안된 노드들의 루트 노드 값을 새로 갱신함
            a = union_parent(node1)
            b = union_parent(node2)

            # 서로 연결이 되어 있는데 루트 노드 값이 갱신이 안되어 연결이 안 된 것으로 판단하는 경우를 방지
            # 루트 노드가 다른 경우에만 노드를 연결한다.
            if a != b:
                # 루트 노드를 서로 연결
                parent[b] = parent[a]
                cost += L2
                line_num += 1

    # 소수 첫째 자리에서 반올림
    answer = round(cost * E)
    print(f'#{test_case} {answer}')
