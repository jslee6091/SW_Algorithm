import sys

sys.stdin = open("electronic_kart_inputs.txt", 'r')

T = int(input())


# 1에서 출발하여 2부터 N 까지의 지점을 모두 돌고 다시 1로 돌아올때 발생하는 비용의 최소값을 구하는 완전 검색 문제
# 참고 URL : https://tothefullest08.github.io/algorithm/2019/08/01/2_5189_%EC%A0%84%EC%9E%90%EC%B9%B4%ED%8A%B8/
def dfs(start):
    global sub_result, result, final_result

    if len(sub_result) == N - 1:
        for i, j in sub_result:
            result += battery[i][j]

        result += battery[start][0]
        final_result.append(result)
        result = 0
        return

    for next in range(1, N):
        if not visited[next]:
            sub_result.append((start, next))
            visited[next] = True
            dfs(next)
            sub_result.remove((start, next))
            visited[next] = False


for test_case in range(1, T + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result = []
    result = 0
    final_result = []
    dfs(0)

    print(f'#{test_case} {min(final_result)}')
