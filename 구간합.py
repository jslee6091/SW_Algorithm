import sys

sys.stdin = open("구간합_inputs.txt", 'r')

T = int(input())


def divide_list(lists, n):
    for i in range(len(lists) - n + 1):
        yield lists[i:i + n]


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    v = list(map(int, input().split()))
    v = list(divide_list(v, M))

    v_sum = []
    v_sum_num = 0

    for idx in v:
        v_sum.append(sum(idx))

    v_sum = sorted(v_sum)
    answer = v_sum[len(v_sum) - 1] - v_sum[0]

    print(f'#{T} {answer}')
