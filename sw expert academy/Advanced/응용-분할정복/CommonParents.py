import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 트리의 두 노드의 공통 부모를 구하는 문제
# 한 노드의 부모를 모두 조사한 후 두번째 노드의 부모와 비교하는 방식으로 구현
for test_case in range(1, 1 + T):
    # V : 정점의 수, E : 간선의 수
    V, E, Node1, Node2 = map(int, input().split())
    # 간선 정보
    line = list(map(int, input().split()))
    # 트리
    tree_parent = [[] for _ in range(V + 1)]
    tree_child = [[] for _ in range(V + 1)]
    # 공통 부모
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

    # 두번째 노드의 부모 구하기 - 첫번째 노드의 부모가 나올때까지
    temp2 = Node2
    while temp2 != 1:
        # 부모 노드 꺼내기
        temp2 = tree_parent[temp2].pop()

        # 첫번째 노드의 부모인 경우 - 이미 꺼냈으므로 빈 리스트이어야 함
        if len(tree_parent[temp2]) == 0:
            commonParent = temp2
            break

    # 공통 부모의 서브 트리 크기 구하기(자기 자신 포함)
    subTree = 0
    # 자식 노드 리스트
    temp3 = [commonParent]
    # 자식 노드 존재하면 실행
    while temp3:
        # 노드 하나씩 꺼내서 개수 1 증가
        child = temp3.pop()
        subTree += 1
        # 꺼낸 노드의 자식 노드 탐색하여 자식 노드 리스트에 추가
        while tree_child[child]:
            temp3.append(tree_child[child].pop())

    print(f'#{test_case} {commonParent} {subTree}')
