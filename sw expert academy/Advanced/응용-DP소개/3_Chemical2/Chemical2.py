import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 1_FindMatrix 와 2_MetalRod 의 응용문제
# 2차원 배열 내의 0이 아닌 수로 이루어진 행렬을 찾고 이들을 곱셈이 가능하도록 정렬
# 연쇄행렬 최소곱셈 알고리즘 적용하여 행렬의 최소곱셈수 구하기
def getmatrix(y, x):
    x_size = 0
    y_size = 0
    # 각 행에 대하여 열의 크기를 구하고 검색완료한 요소는 0으로 변환
    while warehouse[y][x]:
        y_size += 1
        x_temp_size = 0
        # 열에 대한 탐색 및 0으로 변환
        while warehouse[y][x]:
            x_temp_size += 1
            warehouse[y][x] = 0
            x += 1

            if x == N:
                break
        y += 1
        # 다음 행의 열에 대한 탐색을 위해서 x 값 원위치로 옮김
        x -= x_temp_size
        # 열 크기 저장
        x_size = x_temp_size

        if y == N:
            break

    return y_size, x_size


def connect(mat, count):
    global get_equation

    # 행렬 식을 완성한 경우
    if count == len(arr):
        get_equation = mat
        return

    # 행렬 곱셈 식을 만드는 모든 경우를 탐색하고 조건에 따라 가지치기 실행
    for i in range(len(arr)):
        if not is_visited[i]:
            # 행렬 곱셈 식이 맞는 경우 실행 - 아무 식이 없는 경우와 식의 끝 행렬의 열의 크기와 새 행렬의 행의 크기가 일치하는 경우
            if not mat or mat[len(mat) - 1] == arr[i][0]:
                is_visited[i] = 1
                connect(mat + arr[i], count + 1)
                is_visited[i] = 0

    return


# 연쇄행렬 최소곱셈 알고리즘
def min_multiple():
    global get_equation

    d = []
    for idx, var in enumerate(get_equation):
        if idx % 2 == 0 or idx == len(get_equation) - 1:
            d.append(var)

    # 행렬의 개수
    size = len(get_equation) // 2
    # 곱셈 수 저장 리스트
    dp = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size - i):
            a = j
            b = j + i
            if a != b:
                dp[a][b] = 987654
                for k in range(a, b):
                    dp[a][b] = min(dp[a][b], dp[a][k] + dp[k + 1][b] + d[j - 1] * d[k] * d[b])
    
    return dp[0][size - 1]


for test_case in range(1, 1 + T):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]
    arr = []

    row = 0

    while row < N:
        col = 0
        while col < N:
            if warehouse[row][col] != 0:
                # 행렬의 크기 구함
                row_size, col_size = getmatrix(row, col)
                # 행렬 정보 저장
                arr.append((row_size, col_size))
                # 탐색한 행렬의 크기만큼 이동 - 이미 검색했고 행렬 사이에 0이 무조건 들어가있으므로
                col += col_size
            col += 1
        row += 1

    is_visited = [0 for _ in range(len(arr))]
    get_equation = []
    # 행렬 곱셈을 위해 정렬
    connect((), 0)

    # 최소 곱셈 수 구하기
    answer = min_multiple()
    print(f'#{test_case} {answer}')
