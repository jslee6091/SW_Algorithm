import sys

sys.stdin = open('inputs.txt', 'r')

T = int(input())

# 확률 계산 문제 - N 자리의 수에서 각 자릿수가 중복이 되지 않을 확률 구하기 문제
for test_case in range(1, 1 + T):
    N = int(input())

    # 분자
    numerator = 1
    # 분모
    denominator = 1

    # 분자와 분모 구하기 - N이 1인경우 1이 된다.
    for i in range(N):
        if i == 0:
            numerator *= 9
            denominator *= 9
        else:
            numerator *= (10 - i)
            denominator *= 10

    answer = round(numerator / denominator, 5)
    print(f'#{test_case} ', end='')
    # 반올림 한 후 소수점 5자리까지 출력하기
    print('%.5f' % answer)
