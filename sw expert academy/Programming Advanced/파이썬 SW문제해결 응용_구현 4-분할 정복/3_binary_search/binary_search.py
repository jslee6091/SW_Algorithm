import sys
sys.stdin = open("binary_search_inputs.txt", 'r')

T = int(input())

# 이진 탐색 하면서 왼쪽 오른쪽 방향으로 번갈아가며 탐색하는 경우를 찾는 문제
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    answer = 0

    for i in B:
        start = 0
        end = len(A) - 1

        # 진행 방향 -> 1 이면 오른쪽, -1 이면 왼쪽
        direction = 0

        while start <= end:
            mid = (start + end) // 2

            if i == A[mid]:
                answer += 1
                break

            # 중간값이 찾는 값보다 클 때
            elif i < A[mid]:
                end = mid - 1
                # 이전의 방향과 같은 경우 break
                if direction == -1:
                    break
                direction = -1

            # 중간값이 찾는 값보다 작을 때
            elif i > A[mid]:
                start = mid + 1
                # 이전의 방향과 같은 경우 break
                if direction == 1:
                    break
                direction = 1

    print(f'#{test_case} {answer}')
