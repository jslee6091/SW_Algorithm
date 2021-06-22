import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# BackTracking 문제 - N 개의 지점을 한번씩 모두 지나가는 최소 거리의 경로 구하기
# 깊이우선탐색과 가지치기 활용하여 문제 해결
# 가지치기로 탐색 횟수를 줄였지만 그럼에도 실행 시간은 조금 길다.
def dfs(number, location, temp2):
    global distance

    # 현재 누적 거리 temp2가 전체 최소 거리 distance 보다 크거나 같고 distance 가 0보다 클때 거리 계산 x(가지치기)
    # 초기에는 temp2와 distance 둘다 0 이므로 거리 계산을 해야 함
    if temp2 >= distance != 0:
        return

    # N 개의 지점을 모두 지나갔을 때
    if number == N:
        # 최종 목적지 까지 거리 계산
        temp3 = abs(location[0] - home[0]) + abs(location[1] - home[1])

        # 현재까지 누적 거리 temp2와 최종 목적지 사이의 거리를 합한 값이 최소값인 경우 갱신
        # distance 가 0 인 경우 초기값이므로 무조건 갱신
        if distance == 0 or distance > temp2 + temp3:
            distance = temp2 + temp3

        return

    # N 개의 지점을 하나씩 차례로 방문하는 모든 경우 고려
    for idy, var in enumerate(clients):
        # 만약 현재 방문하지 않았다면 방문
        if not is_visited[idy]:
            # 이전 방문 지점과 현재 지점 사이의 거리 계산
            temp3 = abs(location[0] - var[0]) + abs(location[1] - var[1])
            # 방문 했음을 표시
            is_visited[idy] = 1
            # 다음 지점으로 방문
            dfs(number + 1, var, temp2 + temp3)
            # 모든 경우의 거리 계산 위해 방문 하지 않은 것으로 다시 바꿈
            is_visited[idy] = 0

    return distance


for test_case in range(1, 1 + T):
    N = int(input())
    coordinate = list(map(int, input().split()))
    # 회사 위치
    company = coordinate[:2]
    # 집 위치
    home = coordinate[2:4]
    # N 개의 지점 위치
    clients = []
    for idx, num in enumerate(coordinate[4:]):
        if idx % 2 == 0:
            clients.append([num, coordinate[5 + idx]])

    distance = 0
    is_visited = [0 for _ in range(N)]
    dfs(0, company, 0)

    print(f'#{test_case} {distance}')
