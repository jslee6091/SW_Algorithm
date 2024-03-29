import sys

sys.stdin = open("maze2_inputs.txt", 'r')

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# maze1 문제에서 미로의 크기가 100*100으로 바뀐 문제
# maze1 문제와 같이 BFS(깊이우선탐색) 을 적용하여 해결
for test_case in range(1, 11):
    N = input()
    maze = [list(map(int, input())) for _ in range(100)]
    start_col = 0
    start_row = 0
    answer = 0

    for i in maze:
        if 2 in i:
            start_col = i.index(2)
            break
        start_row += 1

    # BFS(너비우선탐색)에 활용할 Queue
    bfs_queue = [(start_row, start_col)]

    # Queue 에 원소가 있으면 탐색 실행, 없으면 탐색 종료
    while bfs_queue:
        check = bfs_queue.pop(0)
        for row, col in move:
            next_row = check[0] + row
            next_col = check[1] + col

            # 미로를 벗어나는 경우는 pass
            if next_row == -1 or next_row == 100 or next_col == -1 or next_col == 100:
                continue

            # 0인 경우 다음 탐색 위치이므로 Queue 에 저장
            if maze[next_row][next_col] == 0:
                bfs_queue.append((next_row, next_col))
            elif maze[next_row][next_col] == 3:
                answer = 1
                break

        maze[check[0]][check[1]] = 1
        if answer:
            break

    print(f'#{test_case} {answer}')
