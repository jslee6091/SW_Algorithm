import sys
sys.stdin = open("최소신장트리_inputs.txt", 'r')

T = int(input())


# Kruskal 알고리즘을 이용하여 최소 신장 트리(Spunning Tree) 구하고 최종 가중치 합 구하기
def union_parent(z):
    if p[z] != z:
        p[z] = union_parent(p[z])
    return p[z]


def union_find(x, y):
    a = union_parent(x)
    b = union_parent(y)

    p[a] = b


for test_case in range(1, T + 1):
    # V + 1 : 노드의 개수, E : 간선의 개수
    V, E = map(int, input().split())
    gajungchee = [list(map(int, input().split())) for _ in range(E)]
    p = [i for i in range(V + 1)]

    # 가중치를 기준으로 정렬
    gajungchee.sort(key=lambda x: x[2])

    answer = 0
    # 간선의 개수
    tree_num = 0
    while gajungchee:
        # 모든 트리를 연결하면 더이상의 탐색을 중지하고 break -> 이거 안했더니 시간초과 발생했다.
        if tree_num == V:
            break
        # u, v : 연결된 노드, cost : 가중치
        u, v, cost = gajungchee.pop(0)
        # 노드가 서로 연결되어있지 않으면 (부모가 다르면) 가중치 더하고 서로 연결함
        if union_parent(u) != union_parent(v):
            union_find(u, v)
            answer += cost
            # 간선 한개 추가
            tree_num += 1

    print(f'#{test_case} {answer}')
