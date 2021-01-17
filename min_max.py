import sys

sys.stdin = open("min_max_inputs.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = map(int, input().split(' '))
    num_list = sorted(num_list)
    print(f'#{test_case} {num_list[N-1]-num_list[0]}')
    num_list.clear()
