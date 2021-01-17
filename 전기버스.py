import sys

sys.stdin = open("전기버스_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split(' '))

    # 충전기 위치 정보
    charge_list = list(map(int, input().split(' ')))

    # 충전기 위치를 표시할 리스트 - N+1개의 0으로 초기화
    charge_check = [0] * (N + 1)

    # 충전기 위치 = n 일때 n번째 요소값 = 1
    for i in range(len(charge_list)):
        charge_check[charge_list[i]] += 1

    location = 0
    end = K
    answer = 0

    while True:
        check = 0
        for j in range(location + 1, end + 1):
            if charge_check[j] == 1:
                location = j
            else:
                check += 1

        # check = K이면 충전기가 없으므로 정답은 0
        if check == K:
            answer = 0
            break

        answer += 1

        # 그 다음 K번 조회를 위한 end 값 설정
        end = location + K

        # N개의 정류장 모두 조회 완료
        if end >= N:
            break

    print(f'#{test_case} {answer}')
