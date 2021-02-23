import sys
sys.stdin = open("BinaryHeap_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    heap = [0]
    answer = 0

    for i in map(int, input().split()):
        heap.append(i)
        child = heap.index(i)
        parent = heap.index(i) // 2

        while heap[child] < heap[parent]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = parent // 2

    index = (len(heap)-1) // 2
    while index > 0:
        answer += heap[index]
        index = index // 2

    print(f'#{test_case} {answer}')
