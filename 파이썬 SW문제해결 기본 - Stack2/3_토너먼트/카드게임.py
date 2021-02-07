import sys

sys.stdin = open("카드게임_inputs.txt", 'r')

T = int(input())


def win(a, b):
    # a가 이기는 경우
    if (cards[a - 1] == 1 and cards[b - 1] == 3) or (cards[a - 1] == 1 and cards[b - 1] == 1):
        return a
    elif (cards[a - 1] == 2 and cards[b - 1] == 1) or (cards[a - 1] == 2 and cards[b - 1] == 2):
        return a
    elif (cards[a - 1] == 3 and cards[b - 1] == 2) or (cards[a - 1] == 3 and cards[b - 1] == 3):
        return a

    # if 문을 만족하지 못한 경우 b가 승리
    return b


def tournament(start, end):
    if start == end:
        return start

    group1 = tournament(start, (start + end) // 2)
    group2 = tournament((start + end) // 2 + 1, end)
    return win(group1, group2)


for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    first = 1
    last = N
    answer = tournament(first, last)
    print(f'#{test_case} {answer}')
