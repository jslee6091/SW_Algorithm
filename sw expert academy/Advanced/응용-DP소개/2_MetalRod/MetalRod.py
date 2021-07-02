import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def connect(stick, count):
    global max_num, answer

    if count > N:
        return

    if count > max_num:
        max_num = count
        answer = stick

    for i in range(len(rods)):
        if not is_visited[i]:
            if not stick or stick[len(stick) - 1] == rods[i][0]:
                is_visited[i] = 1
                connect(stick + rods[i], count + 1)
                is_visited[i] = 0

    return


for test_case in range(1, 1 + T):
    N = int(input())
    rod_info = list(map(int, input().split()))
    rods = []
    for idx, var in enumerate(rod_info):
        if idx % 2 == 0:
            rods.append((var, rod_info[idx + 1]))

    answer = []
    max_num = 0
    is_visited = [0 for _ in range(N)]

    connect((), 0)

    print(f'#{test_case} ', end='')
    for j in answer:
        print(j, end=' ')
    print()
