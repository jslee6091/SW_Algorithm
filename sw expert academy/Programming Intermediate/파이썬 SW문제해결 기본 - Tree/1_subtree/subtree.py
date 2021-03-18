import sys
sys.stdin = open("subtree_imputs.txt", 'r')

T = int(input())


def subtree(num):
    number = 1
    if len(nodes[num-1]) != 0:
        for i in nodes[num-1]:
            number += subtree(i)
    else:
        return number

    return number


for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = [[] for _ in range(E + 1)]
    node_info = list(map(int, input().split()))
    index = 0

    for idx, var in enumerate(node_info):
        if idx % 2 == 0:
            index = var
        else:
            nodes[index-1].append(var)

    answer = subtree(N)
    print(f'#{test_case} {answer}')
