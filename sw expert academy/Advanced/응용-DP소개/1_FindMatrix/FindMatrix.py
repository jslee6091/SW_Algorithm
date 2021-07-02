import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


# 동적 계획법 - 2차원 배열에서 0이 아닌 한자리수로 이루어진 행렬 찾기
def getinfo(y, x):
    x_size = 0
    y_size = 0
    # 각 행에 대하여 열의 크기를 구하고 검색완료한 요소는 0으로 변환
    while matrix[y][x]:
        y_size += 1
        x_temp_size = 0
        # 열에 대한 탐색 및 0으로 변환
        while matrix[y][x]:
            x_temp_size += 1
            matrix[y][x] = 0
            x += 1
        y += 1
        # 다음 행의 열에 대한 탐색을 위해서 x 값 원위치로 옮김
        x -= x_temp_size
        # 열 크기 저장
        x_size = x_temp_size

    return y_size, x_size


for test_case in range(1, 1 + T):
    # 2차원 배열의 크기 - N * N
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 행렬 정보 리스트
    info = []

    row = 0

    # 2차원 배열의 요소 하나씩 탐색하여 0이 아닌 수의 행렬을 찾는다.
    while row < N:
        col = 0
        while col < N:
            # 0이 아닌 경우 행렬이 있음
            if matrix[row][col] != 0:
                # 행렬의 크기 구함
                row_size, col_size = getinfo(row, col)
                # 행렬 정보 저장
                info.append((row_size, col_size, row_size * col_size))
                # 탐색한 행렬의 크기만큼 이동 - 이미 검색했고 행렬 사이에 0이 무조건 들어가있으므로
                col += col_size
            col += 1
        row += 1

    # 행렬의 크기 순서로 오름차순 정렬, 같을 경우 행의 크기 순서로 오름차순 정렬
    info.sort(key=lambda x: (x[2], x[0]))
    # 출력
    print(f'#{test_case} {len(info)}', end=' ')
    for i in info:
        print(i[0], i[1], end=' ')
    print()
