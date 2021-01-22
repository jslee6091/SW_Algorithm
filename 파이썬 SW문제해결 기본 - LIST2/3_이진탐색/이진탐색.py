import sys

sys.stdin = open("이진탐색_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    centerA = 0
    centerB = 0
    left_a = 1
    left_b = 1
    right_a = P
    right_b = P

    answer = 0

    while True:
        centerA = int((left_a+right_a)/2)
        if centerA < A:
            left_a = centerA
        else:
            right_a = centerA

        centerB = int((left_b + right_b) / 2)
        if centerB < B:
            left_b = centerB
        else:
            right_b = centerB

        if centerA == A and centerB == B:
            answer = 0
            break
        elif centerA != A and centerB == B:
            answer = 'B'
            break
        elif centerA == A and centerB != B:
            answer = 'A'
            break

    print(f'#{test_case} {answer}')
