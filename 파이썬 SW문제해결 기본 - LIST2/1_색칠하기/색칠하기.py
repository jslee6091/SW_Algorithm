import sys

sys.stdin = open("색칠하기_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    num_list = [0] * 10
    for i in range(10):
        num_list[i] = [0] * 10

    for ind in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for nemo1 in range(r1, r2 + 1):
            for nemo2 in range(c1, c2 + 1):
                num_list[nemo1][nemo2] += color

    for check in num_list:
        print(check)

    print(f'{test_case} 번째 배열')

