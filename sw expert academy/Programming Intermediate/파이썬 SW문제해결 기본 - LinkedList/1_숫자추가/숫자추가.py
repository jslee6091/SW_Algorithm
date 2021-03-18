import sys
sys.stdin = open("숫자추가_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    num_list = list(map(int, input().split()))
    for i in range(M):
        index, data = map(int, input().split())
        num_list.insert(index, data)
    print(f'#{test_case} {num_list[L]}')
