import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 1_FindMatrix 와 2_MetalRod 의 응용문제
# 2차원 배열 내의 0이 아닌 수로 이루어진 행렬을 찾고 이들을 곱셈이 가능하도록 정렬한 후 곱셈 연산 수 구하기
# 연산 순서를 다르게 해서 최소 연산수를 구하는 것이 목표
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

    print('arr : ', arr)

    is_visited = [0 for _ in range(len(arr))]
    get_equation = []
    connect((), 0)
    print('get_equation : ', get_equation)

    get_equation_convert = []
    for idx, var in enumerate(get_equation):
        if idx % 2 == 0:
            get_equation_convert.append((var, get_equation[idx + 1]))
    print('get_equation_convert : ', get_equation_convert)

    multiple_check = []
    for i in range(len(get_equation_convert)):




