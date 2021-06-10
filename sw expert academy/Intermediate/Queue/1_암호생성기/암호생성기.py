import sys
sys.stdin = open("암호생성기_inputs.txt", 'r')

# Queue 의 성질을 이용한 암호생성기 문제
for test_case in range(1, 11):
    N = input()
    arrays = list(map(int, input().split()))
    number = [1, 2, 3, 4, 5]
    index = 0

    while True:
        index %= 5
        arrays.append(arrays.pop(0) - number[index])
        if arrays[-1] <= 0:
            arrays[-1] = 0
            break
        index += 1

    # print(f'#{test_case} {*arrays}') 를 할 수 없으므로 end 를 이용하여 나누어서 표현
    # asterisk 는 값 삽입이 안되고 print 에서도 asterisk 이 붙은 변수 하나만 입력 가능하다.
    print(f'#{test_case} ', end='')
    print(*arrays)
