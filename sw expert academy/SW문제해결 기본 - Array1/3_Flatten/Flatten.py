import sys

sys.stdin = open("Flatten_inputs.txt", 'r')

T = 10


for test_case in range(1, T + 1):
    dump = int(input())
    box_heights = list(map(int, input().split()))

    for _ in range(dump):
        if max(box_heights) - min(box_heights) <= 1:
            break

        box_heights[box_heights.index(max(box_heights))] -= 1
        box_heights[box_heights.index(min(box_heights))] += 1
    else:
        pass

    answer = max(box_heights) - min(box_heights)
    print(f'#{test_case} {answer}')
