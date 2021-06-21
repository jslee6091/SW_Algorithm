import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(number, location, temp2):
    global distance

    if number == N:
        temp2 += abs(location[0] - home[0]) + abs(location[1] - home[1])
        distance = temp2
        return

    if temp2 >= distance:
        for idy, var in enumerate(clients):
            if not is_visited[idy]:
                temp3 = abs(location[0] - var[0]) + abs(location[1] - var[1])
                is_visited[idy] = 1
                dfs(number + 1, var, temp2 + temp3)
                is_visited[idy] = 0
    else:
        return

    return distance


for test_case in range(1, 1 + T):
    N = int(input())
    coordinate = list(map(int, input().split()))
    company = coordinate[:2]
    home = coordinate[2:4]
    clients = []
    for idx, num in enumerate(coordinate[4:]):
        if idx % 2 == 0:
            clients.append([num, coordinate[5 + idx]])

    distance = -1
    is_visited = [0 for _ in range(N)]
    dfs(0, company, 0)

    print(distance)