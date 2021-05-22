import sys
sys.stdin = open("SortedSubset_inputs.txt", 'r')

# 참고 : https://daep93.github.io/2020/05/14/SW-5262/
# 원소의 순서가 원래 집합 내 순서와 일치하고 정렬이 필요없는 부분집합을 구하는 문제
T = int(input())

for test_case in range(1, T + 1):

    N, *tokens = map(int, input().split())
    numbers = list(tokens)
    len_list = [0 for _ in range(N)]

    for idx in range(N):
        if idx == 0:
            len_list[idx] = 1

        else:
            max_val = 0
            last = numbers[idx]

            for sub_idx in range(idx):
                if numbers[sub_idx] <= last and max_val < len_list[sub_idx]:
                    max_val = len_list[sub_idx]

            len_list[idx] = max_val + 1

    answer = max(len_list)
    print(f'#{test_case} {answer}')
