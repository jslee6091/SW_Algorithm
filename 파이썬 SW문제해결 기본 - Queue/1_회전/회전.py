import queue
import sys

sys.stdin = open("회전_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    num_list = queue.Queue()
    for i in map(int, input().split()):
        num_list.put(i)

    for i in range(M):
        temp = num_list.get()
        num_list.put(temp)

    answer = num_list.get()
    print(f'#{test_case} {answer}')
