import sys
sys.stdin = open("암호_inputs.txt", 'r')

T = int(input())


for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    index = 0
    for _ in range(K):
        index += M
        if index > len(num_list):
            index -= len(num_list)

        if not index:
            num_list.insert(0, num_list[-1] + num_list[0])
        elif index == len(num_list):
            num_list.append(num_list[-1] + num_list[0])
        else:
            num_list.insert(index, num_list[index - 1] + num_list[index])

    answer = list(reversed(num_list))
    if len(answer) > 10:
        answer = answer[:10]
    print(f'#{test_case}', *answer)
