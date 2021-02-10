import sys
import queue

sys.stdin = open("미로의_거리_inputs.txt", 'r')

T = int(input())
moving = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs():
    global track
    count = 0

    while not track.empty():
        second_track = queue.Queue()

        while not track.empty():
            check = track.get()
            row = check[0]
            col = check[1]

            for y, x in moving:
                next_row = row + y
                next_col = col + x

                if 0 <= next_col < N and 0 <= next_row < N:

                    if maze[next_row][next_col] == 0:
                        second_track.put([next_row, next_col])
                        maze[next_row][next_col] = 1

                    if maze[next_row][next_col] == 3:
                        return count

        count += 1
        track = second_track

    return 0


for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    track = queue.Queue()

    for i in maze:
        for j in i:
            if j == 2:
                track.put([maze.index(i), i.index(j)])
                break
        else:
            continue

    answer = bfs()
    print(f'#{test_case} {answer}')
