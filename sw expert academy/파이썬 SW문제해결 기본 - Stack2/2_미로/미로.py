import sys

sys.stdin = open("미로_inputs.txt", 'r')

T = int(input())

moving = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check_boundary(check_y, check_x, n):
    if check_y < 0 or check_x < 0 or check_y >= n or check_x >= n:
        return True
    else:
        return False


for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    start_row = 0
    start_col = 0
    answer = 0

    for num in range(N):
        if 2 in maze[num]:
            start_col = maze[num].index(2)
            start_row = num
            break

    track = [(start_row, start_col)]

    while track:
        row, col = track.pop()
        maze[row][col] = 1

        for y, x in moving:
            next_y = row + y
            next_x = col + x

            if check_boundary(next_y, next_x, N):
                continue

            if maze[next_y][next_x] == 3:
                answer = 1
                break

            elif maze[next_y][next_x] == 0:
                track.append([next_y, next_x])
        else:
            continue

        break

    print(f'#{test_case} {answer}')
