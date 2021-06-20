import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    # V : 정점의 수, E : 간선의 수
    V, E, Node1, Node2 = map(int, input().split())
    # 간선 정보
    line = list(map(int, input().split()))
    # 트리
    tree_parent = [[] for _ in range(V + 1)]
    tree_child = [[] for _ in range(V + 1)]

    commonParent = 0

    # 간선 연결 - 부모 구하기 용도
    for idx, num in enumerate(line):
        if idx % 2 == 1:
            tree_parent[num].append(line[idx - 1])
    # 간선 연결 - 자식 구하기 용도
    for idx, num in enumerate(line):
        if idx % 2 == 0:
            tree_child[num].append(line[idx + 1])

    # 첫번째 노드의 부모 노드 구하기
    node1parents = []
    # 시작 노드
    temp = Node1
    while temp != 1:
        node1parents.append(temp)
        temp = tree_parent[temp].pop()
    print(node1parents)

    # 두번째 노드의 부모 구하기 - 첫번째 노드의 부모가 나올때까지
    temp2 = Node2
    while temp2 != 1:
        # 첫번째 노드의 부모인 경우
        if len(tree_parent[temp2]) == 0:
            commonParent = temp2
            break
        temp2 = tree_parent[temp2].pop()

    print(commonParent)