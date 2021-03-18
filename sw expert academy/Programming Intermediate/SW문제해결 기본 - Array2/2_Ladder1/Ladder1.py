import sys
sys.stdin = open("Ladder1_inputs.txt", 'r')

for test_case in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    conv = sum(ladder, [])

    location = conv.index(2)

    # 위쪽: -100, 아래쪽: +100, 왼쪽: -1, 오른쪽: +1
    while location >= 100:

        if location == len(conv) - 1:
            location -= 100

        if conv[location - 1] == 1 and location % 100 != 0:
            while conv[location - 1] != 0:
                conv[location] = 0
                location -= 1
                if location % 100 == 0:
                    break

        elif conv[location + 1] == 1 and location % 100 != 99:
            while conv[location + 1] != 0:
                conv[location] = 0
                location += 1
                if (location + 1) % 100 == 0:
                    break

        else:
            conv[location] = 0
            location -= 100

    answer = location
    print(f'#{test_case} {answer}')
