import sys

sys.stdin = open("숫자카드_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = [0] * 10

    K = list(map(int, input()))

    for var in K:
        num_list[var] += 1

    card_num = 0
    card_count = 0

    for idx, num in enumerate(num_list):
        if num > card_count:
            card_count = num
            card_num = idx
        elif num == card_count:
            card_num = idx
        else:
            pass

    print(f'#{test_case} {card_num} {card_count}')
