import sys

sys.stdin = open("min_sum_inputs.txt", 'r')

T = int(input())


# 완전 검색을 이용하여 최소합을 갖는 경로와 합을 탐색하는 문제
# recursive 한 방법으로 모든 경로를 탐색하여 최소값을 구함
# 이 코드로는 시간 초과가 발생하여 통과하지는 못하고 아래의 다른 코드를 참고하였음
def path_search(row, col, num):
    global sum_result
    num += num_arr[row][col]

    # 목적지에 도착했을 때 더한 값을 저장하고 return
    if row == N - 1 and col == N - 1:
        if sum_result == 0 or sum_result > num:
            sum_result = num
        return

    # 한칸 아래로 이동
    if row + 1 != N:
        path_search(row + 1, col, num)

    # 한칸 오른쪽으로 이동
    if col + 1 != N:
        path_search(row, col + 1, num)

    return


for test_case in range(1, 1 + T):
    N = int(input())
    num_arr = [list(map(int, input().split())) for _ in range(N)]
    sum_result = 0

    path_search(0, 0, 0)

    print(f'#{test_case} {sum_result}')


"""
https://hongsj36.github.io/2020/01/28/Ad_BruteForce/#5188-%EC%B5%9C%EC%86%8C%ED%95%A9-d3
위 URL에서 참고한 코드 - 이 코드는 시간 초과가 발생하지 않았는데 이유는 잘 모르겠다.

def DFS(row, col):
    down = right = N * 11  # 범위 밖 가상의 값

    if row == col >= N - 1:  # 마지막 지점 도착
        return my_map[row][col]
    else:
        if row < N - 1:  # 아래쪽 끝이 아니면
            down = DFS(row + 1, col)
        if col < N - 1:  # 오른쪽 끝이 아니면
            right = DFS(row, col + 1)

    if down < right:  # 작은 값 취함
        return down + my_map[row][col]
    else:
        return right + my_map[row][col]


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test_case, DFS(0, 0)))
"""