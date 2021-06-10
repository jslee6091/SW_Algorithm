import sys
sys.stdin = open("중위순회_inputs.txt", 'r')


def tree_search(index):
    # 자식 노드가 있는 경우
    if nodes[index]:
        # 왼쪽 자식 부터 탐색
        tree_search(nodes[index].pop(0))
    else:
        # 자식 노드 없으면 데이터 저장
        answer.append(node_info[index])
        return

    # 부모 노드 저장
    answer.append(node_info[index])

    # 오른쪽 자식 노드가 있는 경우 탐색 수행
    if nodes[index]:
        tree_search(nodes[index].pop(0))


# 완전 이진 트리 중위순회
for test_case in range(1, 11):
    # 노드의 개수
    node_num = int(input())
    # 자식 노드에 대한 정보
    nodes = [[] for _ in range(node_num + 1)]
    # 노드에 저장된 데이터
    node_info = [0]
    # 정답을 저장할 리스트
    answer = []

    # 리스트에 노드 정보 입력
    for i in range(node_num):
        info = input().split()
        node_info.append(info[1])

        # 자식 노드가 1개 이상인 경우
        if len(info) >= 3:
            for var in info[2:]:
                nodes[int(info[0])].append(int(var))

    # 루트 노드의 인덱스가 1 이므로 1부터 시작
    tree_search(1)

    # 여러 문자열로 구성된 리스트를 하나의 문자열로 통합
    answer = ''.join(answer)
    print(f'#{test_case} {answer}')
