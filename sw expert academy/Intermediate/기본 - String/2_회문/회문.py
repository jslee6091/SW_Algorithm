import sys
sys.stdin = open("회문_inputs.txt", 'r')

T = int(input())


def check_list(check):
    result = True
    for idx in range(int(len(check)/2)):
        if check[idx] != check[len(check)-1-idx]:
            result = False
            break

    return result


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    num_lists = []
    num_lists_rotate = []
    answer = ''

    for i in range(N):
        num_lists.append(list(input()))

    # 가로 방향
    for i in num_lists:
        for j in range(N-M+1):
            if check_list(i[j:j+M]):
                answer = "".join(i[j:j+M])

    # 리스트 회전
    for var in zip(*num_lists):
        num_lists_rotate.append(list(var))

    # 세로 방향
    for i in num_lists_rotate:
        for j in range(N-M+1):
            if check_list(i[j:j+M]):
                answer = "".join(i[j:j+M])

    print(f'#{test_case} {answer}')
