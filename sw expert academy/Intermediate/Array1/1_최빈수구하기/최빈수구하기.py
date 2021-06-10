import sys
sys.stdin = open("최빈수구하기_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    count = [0 for _ in range(101)]
    maximum = 0
    answer = 0

    for num in map(int, input().split()):
        count[num] += 1

    for idx, var in enumerate(count):
        if idx == 0:
            maximum = var
        else:
            if var >= maximum:
                maximum = var
                answer = idx

    print(f'#{test_case} {answer}')
