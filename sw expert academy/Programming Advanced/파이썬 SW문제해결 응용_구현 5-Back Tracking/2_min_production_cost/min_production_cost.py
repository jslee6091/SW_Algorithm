import sys
sys.stdin = open("min_production_cost_inputs.txt", 'r')

T = int(input())


# Back Tracking 을 활용한 최소 비용 연산 문제
# https://tothefullest08.github.io/algorithm/2019/08/31/4_5209_%EC%B5%9C%EC%86%8C%EC%83%9D%EC%82%B0%EB%B9%84%EC%9A%A9/
# 깊이 우선 탐색으로 모든 경우의 비용을 구하는데 중간에 탐색이 필요없는 경우 하지 않고 넘어감
def DFS(y, sum):
    global answer

    # 제품의 수많큼 더한 결과가 이전의 결과보다 작으면 이를 반영
    if y == products:
        if answer > sum:
            answer = sum
        return

    # 탐색 도중 더한 결과가 이전의 결과보다 크면 바로 중지
    if answer < sum:
        return

    # 각 제품의 회사별 가격을 순서대로 탐색함
    for x in range(products):
        if not my_products[x]:
            my_products[x] = True
            DFS(y+1, sum + costs[y][x])
            my_products[x] = False


for test_case in range(1, 1 + T):
    products = int(input())
    costs = [list(map(int, input().split())) for _ in range(products)]
    my_products = [0] * products
    # 문제에서 제품 가격은 100미만이고 개수는 15개 이하이므로 최대가격은 1500을 넘지 않음
    answer = 1500

    DFS(0, 0)

    print(f'#{test_case} {answer}')
