import sys
sys.stdin = open("Ladder2_inputs.txt", 'r')

for test_case in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    result = []
    answer = 0

    for idx, num in enumerate(ladder[0]):
        if num == 1:
            ladder_1dim = sum(ladder, [])
            location = idx
            ladder_1dim[location] = 0
            distance = 0

            while location < len(ladder_1dim) - 100:

                if location == 0:
                    ladder_1dim[location] = 0
                    location += 100
                    distance += 1

                if ladder_1dim[location - 1] == 1 and location % 100 != 0:
                    while ladder_1dim[location - 1] != 0:
                        ladder_1dim[location] = 0
                        location -= 1
                        distance += 1
                        if location % 100 == 0:
                            break

                elif ladder_1dim[location + 1] == 1 and location % 100 != 99:
                    while ladder_1dim[location + 1] != 0:
                        ladder_1dim[location] = 0
                        location += 1
                        distance += 1
                        if (location + 1) % 100 == 0:
                            break

                else:
                    ladder_1dim[location] = 0
                    location += 100
                    distance += 1

            result.append([idx, distance])

    minimum = result[0][1]
    for i in result:
        if i[1] <= minimum:
            minimum = i[1]
            answer = i[0]

    print(f'#{test_case} {answer}')
