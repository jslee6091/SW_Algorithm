import sys

sys.stdin = open("SumOfNodes_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    heap = [0 for _ in range(N + 1)]

    for _ in range(M):
        index, number = map(int, input().split())
        heap[index] = number

    for i in range(N, 0, -1):
        if heap[i] == 0:
            heap[i] = heap[i * 2]
            if i * 2 + 1 < N + 1:
                heap[i] += heap[i * 2 + 1]

    answer = heap[L]
    print(f'#{test_case} {answer}')
