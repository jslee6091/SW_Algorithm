import sys
sys.stdin = open("수열_편집_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    num_list = list(map(int, input().split()))

    for i in range(M):
        info = input().split()
        index = int(info[1])
        if info[0] == 'I':# 추가
            num = int(info[2])
            num_list.insert(index, num)
        elif info[0] == 'D':# 삭제
            del num_list[index]
        elif info[0] == 'C':# 교체
            num = int(info[2])
            num_list[index] = num

    if L >= len(num_list):
        answer = -1
    else:
        answer = num_list[L]

    print(f'#{test_case} {answer}')

