import sys
import queue

sys.stdin = open("미로의_거리_inputs.txt", 'r')

T = int(input())
moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    track = queue.Queue()
    answer = 0

    for i in maze:
        for j in i:
            if j == 2:
                track.put([maze.index(i), i.index(j)])

    while not track.empty():
        check = track.get()
        row = check[0]
        col = check[1]

        for y, x in moving:
            next_row = row + y
            next_col = col + x

            if next_col >= N or next_row >= N or next_row < 0 or next_col < 0:
                continue

            if maze[next_row][next_col] == 3:
                answer += 1
                break

            if maze[next_row][next_col] == 0:
                track.put([next_row, next_col])
                answer += 1
                maze[next_row][next_col] = 1

        else:
            continue

        break

    print(f'#{test_case} {answer}')
