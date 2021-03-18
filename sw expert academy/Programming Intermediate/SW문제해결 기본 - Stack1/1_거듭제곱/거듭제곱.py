import sys
sys.stdin = open("거듭제곱_inputs.txt", 'r')


def square(num, sqr):
    if sqr == 1:
        return num
    return square(num, sqr - 1) * num


for test_case in range(1, 11):
    case = input()
    N, M = map(int, input().split())

    answer = square(N, M)
    print(f'#{test_case} {answer}')
