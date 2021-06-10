import sys
sys.stdin = open("사칙연산_inputs.txt", 'r')


# 트리에 저장된 연산자와 숫자를 계산하는 문제
def tree_operate(index):
    # 노드가 연산자인 경우 자식 노드 탐색
    if type(data[index]) == str:
        left_num = tree_operate(children[index][0])
        right_num = tree_operate(children[index][1])
        
        # 연산자의 종류에 따라 왼쪽 자식과 오른쪽 자식 노드의 값을 연산하여 return
        if data[index] == '+':
            return left_num + right_num
        elif data[index] == '-':
            return left_num - right_num
        elif data[index] == '*':
            return left_num * right_num
        elif data[index] == '/':
            return left_num / right_num
    
    # 노드가 숫자이면 자식 노드가 없으므로 데이터 return
    else:
        return data[index]


for test_case in range(1, 11):
    node_len = int(input())
    # 자식 노드 정보 리스트
    children = [[] for _ in range(node_len + 1)]
    # 노드에 저장된 데이터
    data = [0]
    # 연산식 저장 리스트
    expression = []
    
    # 트리 완성
    for i in range(node_len):
        info = input().split()

        # 노드의 데이터를 data 리스트에 삽입
        # 노드의 데이터가 연산자일 경우에는 그대로 삽입, 숫자일 경유에는 정수로 변환하여 삽입
        if info[1] == '+' or info[1] == '-' or info[1] == '/' or info[1] == '*':
            data.append(info[1])
        else:
            data.append(int(info[1]))

        # 자식 노드가 있는 경우 children 리스트에 추가
        if len(info) >= 3:
            for var in info[2:]:
                children[int(info[0])].append(int(var))

    answer = int(tree_operate(1))
    print(f'#{test_case} {answer}')
