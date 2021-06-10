import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 암호 코드 변환 후 정상 판별 문제
for test_case in range(1, 1 + T):

    # 암호코드가 포함된 2차원 배열 입력받기
    row, col = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]

    # 각 숫자에 대한 암호 - 배열의 인덱스와 매칭
    # ex) 13 - 0, 49 - 5
    cipherNumber = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
    cipherCode = []

    # 2차원 배열에서 암호코드가 있는 배열 얻기
    for i in arr:
        if i[0] > 0:
            cipherCode = list(str(i[0]))
            break

    # 문자열을 정수로 바꾸는 방식으로 암호코드를 얻었으므로 뒤에 붙어있는 숫자 0을 모두 제거한다.
    character = cipherCode.pop()
    while character == '0':
        character = cipherCode.pop()
    cipherCode.append(character)

    index = 0
    number = 0
    cipherDecimal = ''

    # 2진수를 7자리씩 연산하여 10진수로 변환
    while cipherCode:
        num = int(cipherCode.pop())
        number += num * (2 ** index)
        index = (index + 1) % 7
        if index == 0:
            cipherDecimal = str(cipherNumber.index(number)) + cipherDecimal
            number = 0

        # 마지막 7자리 미만의 2진수들이 10진수로 변환된 후 저장
        if len(cipherCode) == 0:
            cipherDecimal = str(cipherNumber.index(number)) + cipherDecimal

    # 변환된 10진수 암호코드에 대한 정상 여부 판별
    cipherList = list(map(int, cipherDecimal))
    # 정답을 위해 미리 코드의 전체 합을 저장
    sum_of_array = sum(cipherList)

    # 홀수번째 코드를 3만큼 곱셈
    for idx, var in enumerate(cipherList):
        if idx % 2 == 0:
            cipherList[idx] *= 3

    # 곱셈한 암호코드의 합이 10으로 나누어 떨어지면 정상 암호코드
    if sum(cipherList) % 10 == 0:
        answer = sum_of_array
    else:
        answer = 0

    print(f'#{test_case} {answer}')

