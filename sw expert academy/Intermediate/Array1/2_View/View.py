import sys

sys.stdin = open("View_inputs.txt", 'r')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    for idx, height in enumerate(buildings):
        if idx == 0 or idx == 1 or idx == N - 1 or idx == N - 2:
            continue

        left = max(buildings[idx - 1], buildings[idx - 2])
        if left >= height:
            continue

        left_num = height - left

        right = max(buildings[idx + 1], buildings[idx + 2])
        if right >= height:
            continue

        right_num = height - right

        answer += min(left_num, right_num)

    print(f'#{test_case} {answer}')
