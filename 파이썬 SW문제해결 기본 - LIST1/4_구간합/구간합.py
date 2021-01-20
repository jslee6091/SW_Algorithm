import sys

sys.stdin = open("구간합_inputs.txt", 'r')

T = int(input())


def divide_list(lists, n):
    for i in range(N - n + 1):
        yield sum(lists[i:i + n])


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    v = list(map(int, input().split()))
    v_sum = list(divide_list(v, M))

    answer = max(v_sum) - min(v_sum)
    print(f'#{test_case} {answer}')
