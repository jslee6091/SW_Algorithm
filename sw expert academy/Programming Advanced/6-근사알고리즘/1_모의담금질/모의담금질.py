import sys
sys.stdin = open("inputs.txt", 'r')

T = int(input())

'''
cost_prev = float('inf')
T = startTemperature
while T > T_end:
    cost_new = cost()
    diff = cost_new - cost_prev
    if difference < 0 or math.exp(-diff/T) > random(0,1):
        cost_prev = cost_new
    T = T * k
'''

# 모의담금질 문제 - 위의 모의담금질 기법에서 cost 함수의 실행 횟수를 구하는 문제
# cost 함수는 따로 구현할 필요 없고 실행 횟수만 구한다.
for test_case in range(1, T + 1):

    T, T_end, K = map(str, input().split())
    # 시작 온도
    T = int(T)
    # 목표 온도 - T가 T_end 미만이 될때까지 연산 실행
    T_end = float(T_end)
    # cooling factor - T가 감소하는 속도와 관련있음
    K = float(K)

    answer = 0

    while T > T_end:
        answer += 1
        T = T * K

    print(f'#{test_case} {answer}')
