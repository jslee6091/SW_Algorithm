import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


# 여러 개의 막대를 최대로 이어 붙이는 문제
# 앞, 뒤에 해당하는 숫자가 주어지고 다른 막대 중 숫자가 맞는 것만 연결 가능
def connect(stick, count):
    global max_num, answer

    # 모든 막대를 연결한 경우
    if count > N:
        return

    # 이미 최댓값을 찾은 경우(가지치기)
    if max_num == N + 1:
        return

    # 현재 막대의 개수가 기존의 최댓값보다 큰 경우 최댓값 갱신, 막대 연결 정보 저장
    if count > max_num:
        max_num = count
        answer = stick

    # 막대를 연결하는 모든 경우를 탐색하고 조건에 따라 가지치기 실행
    for i in range(len(rods)):
        if not is_visited[i]:
            # 이미 연결된 막대의 끝 부분과 새로 연결할 막대의 앞부분의 숫자가 일치하거나 아무것도 연결되어있지 않으면 연결
            if not stick or stick[len(stick) - 1] == rods[i][0]:
                is_visited[i] = 1
                connect(stick + rods[i], count + 1)
                is_visited[i] = 0

    return


for test_case in range(1, 1 + T):
    # 막대 개수와 정보
    N = int(input())
    rod_info = list(map(int, input().split()))
    rods = []
    # 각 막대의 앞, 뒤 숫자를 저장
    for idx, var in enumerate(rod_info):
        if idx % 2 == 0:
            rods.append((var, rod_info[idx + 1]))

    answer = []
    max_num = 0
    # 완전 탐색을 위한 방문 여부 리스트
    is_visited = [0 for _ in range(N)]

    # 탐색 시작
    connect((), 0)

    print(f'#{test_case} ', end='')
    for j in answer:
        print(j, end=' ')
    print()
