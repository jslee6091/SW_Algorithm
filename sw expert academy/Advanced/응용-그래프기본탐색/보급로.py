import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 다익스트라 알고리즘을 활용한 최단 경로 구하기 문제
for test_case in range(1, 1 + T):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    memoization = [[float('inf') for _ in range(N)] for _ in range(N)]

    memoization[0][0] = 0
    dijkstra = [(0, 0)]
    while dijkstra:
        y, x = dijkstra.pop(0)
        for i, j in move:
            if 0 <= y + i <= N - 1 and 0 <= x + j <= N - 1:
                if memoization[y + i][x + j] > memoization[y][x] + maps[y + i][x + j]:
                    memoization[y + i][x + j] = memoization[y][x] + maps[y + i][x + j]
                    dijkstra.append((y + i, x + j))

    print(f'#{test_case} {memoization[N - 1][N - 1]}')
