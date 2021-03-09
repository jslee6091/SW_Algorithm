import sys
sys.stdin = open("길찾기_inputs.txt", 'r')

# DFS(깊이우선탐색) 알고리즘 문제

for test_case in range(1, 11):
    N, load_num = map(int, input().split())
    loads = list(map(int, input().split()))
    node = [[] for _ in range(100)]
    check_stack = [0]
    index = 0
    answer = 0

    for i in range(len(loads)):
        if i % 2 == 0:
            index = loads[i]
        else:
            node[index].append(loads[i])

    while check_stack:
        now_node = check_stack.pop()

        if now_node == 99:
            answer = 1
            break

        if len(node[now_node]) != 0:
            check_stack.append(now_node)
            check_stack.append(node[now_node].pop())

    print(f'#{test_case} {answer}')
