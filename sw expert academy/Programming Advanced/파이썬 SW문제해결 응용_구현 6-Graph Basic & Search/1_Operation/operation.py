from collections import deque
import sys
sys.stdin = open('operation_inputs.txt', 'r')

T = int(input())


# 주어진 숫자 N을 4가지의 연산중 하나를 수행하여 M으로 만들고자 할 때 최소 연산 실행 횟수 구하기 문제
# 4가지 연산 : -1, +1, *2, -10
# 숫자는 연산 과정에서 무조건 1000000 이하의 자연수 이어야 함
# 너비 우선 탐색과 가지치기(pruning), deque 자료구조로 탐색
# 참고 : https://mungto.tistory.com/247
def bfs(N, M):
    # 탐색할 숫자를 담은 deque
    queue = deque()
    queue.append((N, 0))
    # 해당 숫자가 이미 탐색 하였는지 판별하기 위한 dictionary
    check = {}

    while queue:
        # count 는 연산 횟수를 의미
        item, count = queue.popleft()
        # 이미 탐색한 숫자인 경우 continue
        if check.get(item, 0):
            continue
        # item 에 해당하는 숫자를 탐색했음을 표시
        check[item] = 1

        # 정답을 찾은 경우 바로 return
        if item == M:
            return count
        # 정답이 아니면 연산 횟수를 증가
        count += 1

        # 4가지 종류별 연산 결과를 deque 에 저장
        # 만약 연산 결과가 이미 deque 에 들어있는 경우 저장하지 않음
        if 0 < item + 1 <= 1000000 and item + 1 not in queue:
            queue.append((item + 1, count))
        if 0 < item - 1 <= 1000000 and item - 1 not in queue:
            queue.append((item - 1, count))
        if 0 < item * 2 <= 1000000 and item * 2 not in queue:
            queue.append((item * 2, count))
        if 0 < item - 10 <= 1000000 and item - 10 not in queue:
            queue.append((item - 10, count))


for test_case in range(1, 1 + T):
    start_num, end_num = map(int, input().split())

    answer = bfs(start_num, end_num)
    print(f'#{test_case} {answer}')
