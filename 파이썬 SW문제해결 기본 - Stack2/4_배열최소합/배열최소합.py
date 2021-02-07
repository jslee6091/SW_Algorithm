import sys
sys.stdin = open("배열최소합_inputs.txt", 'r')

T = int(input())


def dfs(idx, sub_sum):
    global minimum

    if idx == N:
        if sub_sum < minimum:
            minimum = sub_sum
        return

    # 가지치기 - 검색할 필요가 없는 노드는 검색 안함
    if sub_sum >= minimum:
        return

    for i in range(N):
        if check[i] == 1:
            check[i] = 0
            dfs(idx+1, sub_sum + num_arr[idx][i])
            check[i] = 1


for test_case in range(1, T + 1):
    N = int(input())

    num_arr = [list(map(int, input().split())) for _ in range(N)]
    check = [1]*N
    minimum = 987654321
    dfs(0, 0)
    print(f'#{test_case} {minimum}')
