import sys
sys.stdin = open("electric_bus_inputs.txt", 'r')

T = int(input())

# 충전지의 최소 교환 횟수를 구하는 문제
for test_case in range(1, T + 1):
    stations = list(map(int, input().split()))
    length = stations.pop(0)

    answer = 0
    index = 0
    # 최소 교환 횟수 비교를 위한 리스트
    compare = []

    while index < length - 1:
        # 현재 위치에서 다음 위치가 도착점이 아닐 때
        if index + stations[index] < length - 1:
            for i in range(1, 1 + stations[index]):
                # 인덱스, 리스트 값, 인덱스와 리스트 값의 합
                compare.append((index + i, stations[index + i], index + i + stations[index + i]))

            # 인덱스와 리스트 값의 합으로 내림차순 정렬하여 최대로 갈 수 있는 위치 계산
            compare.sort(key=lambda x: -x[2])
            index = compare[0][0]
            answer += 1
            compare.clear()
        # 현재 위치에서 도착점에 도착할 때
        else:
            answer += 1
            index = length - 1

    # 처음 출발할 때 교환 횟수 차감
    answer -= 1

    print(f'#{test_case} {answer}')
