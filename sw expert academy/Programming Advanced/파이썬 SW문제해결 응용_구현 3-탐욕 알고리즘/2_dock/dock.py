import sys
sys.stdin = open("dock_inputs.txt", 'r')

T = int(input())

# 특정 시각부터 일정 시간동안 도크를 사용하는 여러 화물차에 대해서 24시간동안 도크를 사용한 화물차의 최대값 구하기
for test_case in range(1, T + 1):
    # 화물차 개수 (= 화물차의 사용 신청서 개수)
    apply_num = int(input())
    # 각 화물차의 사용 시작 시간과 종료 시간
    works = [list(map(int, input().split())) for _ in range(apply_num)]
    # 현재 시간
    time = 0
    answer = 0

    # 빨리 끝나는 순서대로 정렬 - 빨리 시작하는 순서대로 정렬하는 것 보다 결과가 더 좋음
    works.sort(key=lambda x: x[1])

    # 도크를 이용한 화물차의 개수 구하기
    while works:
        check = works.pop(0)
        if check[0] < time:
            continue
        else:
            time = check[1]
            answer += 1

    print(f'#{test_case} {answer}')
