import sys
sys.stdin = open("사칙연산_유효성_inputs.txt", 'r')


# 트리에 저장된 숫자 및 연산자들을 중위 순회하여 연산식을 만들고 유효한 식인지를 판단하는 문제
for test_case in range(1, 11):
    node_len = int(input())
    # 자식 노드 정보 리스트
    children = [[] for _ in range(node_len + 1)]
    # 노드에 저장된 데이터
    data = [0]

    answer = 1
    
    # 트리 완성
    for i in range(node_len):
        info = input().split()

        # 노드의 데이터가 연산자일 경우에는 그대로 삽입, 숫자일 경유에는 정수로 변환하여 삽입
        if info[1] == '+' or info[1] == '-' or info[1] == '/' or info[1] == '*':
            data.append(info[1])
        else:
            data.append(int(info[1]))

        # 자식 노드가 있는 경우 children 리스트에 추가
        if len(info) >= 3:
            for var in info[2:]:
                children[int(info[0])].append(int(var))

    # 너비우선탐색으로 트리 순회
    # index 를 queue 에 담아서 탐색
    bfs_queue = [1]

    while bfs_queue:
        index = bfs_queue.pop(0)
        # 노드의 데이터가 연산자인 경우
        if type(data[index]) == str:
            # 자식 노드가 2개 있는 경우
            if len(children[index]) == 2:
                # 자식 노드에 대한 index 를 bfs_queue 에 저장
                while children[index]:
                    bfs_queue.append(children[index].pop(0))
            # 자식 노드가 1개 이하이면 오류이므로 break
            else:
                answer = 0
                break
        # 노드의 데이터가 숫자인 경우
        else:
            # 자식 노드가 있으면 오류이므로 break
            if children[index]:
                answer = 0
                break

    print(f'#{test_case} {answer}')
