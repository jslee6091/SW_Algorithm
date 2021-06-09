import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# a와 b 사이의 모든 소수의 합을 구하는 문제
for test_case in range(1, 1 + T):
    a, b = map(int, input().split())

    answer = 0

    for i in range(a + 1, b):
        is_prime = 1

        # 2부터 숫자의 루트 값 까지만 계산함
        for j in range(2, int(i ** 0.5) + 1):
            # 나누어 떨어지는 경우 소수가 아님
            if i % j == 0:
                is_prime = 0
                break

        # i 가 소수이면 더함
        if is_prime:
            answer += i

    print(f'#{test_case} {answer}')
