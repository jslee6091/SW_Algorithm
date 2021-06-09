import sys

sys.stdin = open("최소이동거리_inputs.txt", 'r')

T = int(input())

# Dijkstra Algorithm 을 이용한 최소 이동 거리 구하기
for test_case in range(1, T + 1):
    # N : 노드의 마지막 번호, E : 간선의 수
    N, E = map(int, input().split())
    # 간선의 정보 - 노드의 개수(N + 1 개)
    load = [[] for _ in range(N + 1)]
    # 노드별 이동 거리 정보
    length = [float('inf')] * (N + 1)
    # 첫번째 노드는 0
    length[0] = 0

    for i in range(E):
        s, e, w = map(int, input().split())
        load[s].append((e, w))

    queue = [0]
    while queue:
        # 현재 위치
        index = queue.pop(0)
        # 현재 노드와 연결된 노드들이 있으면 실행
        while load[index]:
            # 목적지와 거리를 이용해 목적지까지 이동 거리를 계산
            end, distance = load[index].pop(0)
            next_distance = length[index] + distance
            # 만약 해당 노드까지 이동 거리가 더 짧아지면 length 에 값을 저장
            if length[end] > next_distance:
                length[end] = next_distance
                # 다음 탐색할 노드로 저장
                queue.append(end)

    print(f'#{test_case} {length[N]}')
