import sys
sys.stdin = open('GraphColoring_inputs.txt', 'r')


# 그래프 색칠문제 - 인접한 정점이 서로 다른 색을 칠하도록 만들 수 있는지 판단하는 문제
# 참고 : https://velog.io/@eunbani/SWEA-5286-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%83%89%EC%B9%A0%ED%95%98%EA%B8%B0
def graphcoloring():
    # 사용 가능한 전체 색
    colors = set([i for i in range(1, m + 1)])

    for adjV in adjacent:
        # 전체 색에서 인접한 노드들의 색을 제거
        # set 이므로 {0}을 빼면 아무런 변화가 없다.
        colors -= colored[adjV]

    # colors 의 크기가 0이면 현재 사용 가능한 색이 없으므로 False 반환
    if not colors:
        return False

    # 현재 사용가능한 색 중 최소값을 선택하여 배치 - 이것은 최대값으로 선택해도 무방
    colored[v] = {min(colors)}

    # 현재 사용가능한 색이 있으므로 True 반환
    return True


for t in range(1, int(input())+1):
    # n : 정점의 수, e : 간선의 수, m : 색 종류의 개수
    n, e, m = map(int, input().split())
    graph = dict()
    answer = 1

    # 어떤 색으로 칠했는지 저장하는 리스트
    colored = [{0} for _ in range(n+1)]

    # 그래프 간선에 따라 인접 정점 추가
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1] = graph.get(v1, set()).union({v2})
        graph[v2] = graph.get(v2, set()).union({v1})

    # 각 정점 별로 인접 정점의 색과 다르게 색칠한다.
    for v in graph:
        # 인접 점들을 확인
        adjacent = graph[v]

        # graphcoloring 함수 실행 후 더 이상 색칠할 색이 없는 경우 색칠 불가능
        if not graphcoloring():
            answer = 0
            break

    # answer = 1 이면 색칠 가능
    print(f'#{t} {answer}')
