import sys

sys.stdin = open("부분집합_inputs.txt", 'r')

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    check = 0
    check_list = []
    answer = 0

    for i in range(1 << 12):
        for j in range(12):
            if i & (1 << j):
                check += 1
                check_list.append(A[j])

        if check == N:
            if sum(check_list) == K:
                answer += 1

        check = 0
        check_list.clear()

    print(f'#{test_case} {answer}')
