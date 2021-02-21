import queue
import sys
sys.stdin = open("피자_굽기_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    fire = queue.Queue()
    check = [i for i in range(1, N+1)]
    index_count = N
    answer = 0

    for i in range(N):
        fire.put(cheese.pop(0))

    while not fire.empty():
        temp = fire.get()//2
        if temp == 0:
            answer = check.pop(0)
            if len(cheese) > 0:
                fire.put(cheese.pop(0))
                index_count += 1
                check.append(index_count)
            else:
                if fire.empty():
                    break
        else:
            fire.put(temp)
            check.append(check.pop(0))

    print(f'#{test_case} {answer}')
