import sys
sys.stdin = open('inputs.txt', 'r')

T = int(input())

# 서로 다른 정수로 이루어진 두 집합에 모두 들어있는 정수의 개수를 구하는 문제
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    # 두 set 의 합집합
    C = A.union(B)

    # 원래 두 집합의 크기를 더한 후 합집합의 크기를 빼면 교집합의 크기를 알 수 있음
    answer = len(A) + len(B) - len(C)

    # 또한 set 의 intersection 함수를 이용하면 교집합을 바로 구할 수 있음
    answer2 = len(A.intersection(B))

    # 마지막으로 & 연산자로 교집합을 구할 수 있음
    answer3 = len(A & B)

    print(f'#{test_case} {answer}')
